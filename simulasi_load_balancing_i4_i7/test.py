import argparse
import csv
import re
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

DEFAULT_URL = "http://localhost:8085"

def extract_server_name(html: str) -> str:
    pattern = r"WEB SERVER\s+\d+\s+\([^)]+\)"
    match = re.search(pattern, html)
    if match:
        return match.group(0)
    return "Server tidak terdeteksi"

def send_request(index: int, url: str, timeout: int = 15):
    start = time.perf_counter()
    response = requests.get(url, timeout=timeout)
    elapsed = time.perf_counter() - start
    response.raise_for_status()
    server_name = extract_server_name(response.text)
    return index, server_name, elapsed

def main():
    parser = argparse.ArgumentParser(description="Pengujian simulasi load balancing.")
    parser.add_argument("--url", default=DEFAULT_URL, help="URL load balancer. Default: http://localhost:8085")
    parser.add_argument("--requests", type=int, default=20, help="Jumlah request yang dikirim. Default: 20")
    parser.add_argument("--workers", type=int, default=10, help="Jumlah request paralel. Default: 10")
    parser.add_argument("--mode", default="Pengujian", help="Nama skenario, contoh: i4 Round Robin")
    parser.add_argument("--csv", default="", help="Opsional: simpan hasil ke file CSV.")
    args = parser.parse_args()

    print(f"\n=== MULAI {args.mode.upper()} ===")
    print(f"Target URL       : {args.url}")
    print(f"Jumlah request   : {args.requests}")
    print(f"Jumlah worker    : {args.workers}\n")

    results = []

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(send_request, i, args.url)
            for i in range(1, args.requests + 1)
        ]

        for future in as_completed(futures):
            try:
                index, server_name, elapsed = future.result()
                results.append((index, server_name, elapsed, "OK"))
            except Exception as error:
                results.append((-1, str(error), 0, "ERROR"))

    results.sort(key=lambda x: x[0])

    for index, server_name, elapsed, status in results:
        if status == "ERROR":
            print(f"ERROR: {server_name}")
        else:
            print(f"Request {index:02d}: Terarah ke -> {server_name:<28} | waktu: {elapsed:.3f} detik")

    counter = Counter(server for _, server, _, status in results if status == "OK")

    print("\n=== RINGKASAN DISTRIBUSI ===")
    for server, count in sorted(counter.items()):
        print(f"{server}: {count} request")

    if args.csv:
        csv_path = Path(args.csv)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        with csv_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["request_ke", "server_tujuan", "waktu_detik", "status"])
            for index, server_name, elapsed, status in results:
                writer.writerow([index, server_name, f"{elapsed:.4f}", status])
        print(f"\nHasil CSV disimpan ke: {csv_path}")

    print("\nSelesai.\n")

if __name__ == "__main__":
    main()
