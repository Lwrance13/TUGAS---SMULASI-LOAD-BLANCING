import subprocess
import sys
import time
from pathlib import Path

SCENARIOS = [
    ("i4 Round Robin", "docker-compose.i4.roundrobin.yml", "test_i4_roundrobin.py"),
    ("i4 Least Connections", "docker-compose.i4.leastconn.yml", "test_i4_leastconn.py"),
    ("i7 Round Robin", "docker-compose.i7.roundrobin.yml", "test_i7_roundrobin.py"),
    ("i7 Least Connections", "docker-compose.i7.leastconn.yml", "test_i7_leastconn.py"),
]

ALL_COMPOSES = [
    "docker-compose.i4.roundrobin.yml",
    "docker-compose.i4.leastconn.yml",
    "docker-compose.i7.roundrobin.yml",
    "docker-compose.i7.leastconn.yml",
]

def run(cmd, check=False):
    print(">", " ".join(cmd))
    return subprocess.run(cmd, check=check)

def stop_all():
    for compose in ALL_COMPOSES:
        run(["docker", "compose", "-f", compose, "down"])

def main():
    Path("hasil_pengujian").mkdir(exist_ok=True)

    for title, compose, test_file in SCENARIOS:
        print("\n" + "=" * 70)
        print(f"SKENARIO: {title}")
        print("=" * 70)

        stop_all()
        run(["docker", "compose", "-f", compose, "up", "-d", "--build"], check=True)

        print("Menunggu container siap...")
        time.sleep(12)

        run([sys.executable, test_file], check=True)

    stop_all()
    print("\nSemua pengujian selesai. File CSV ada di folder hasil_pengujian.")

if __name__ == "__main__":
    main()
