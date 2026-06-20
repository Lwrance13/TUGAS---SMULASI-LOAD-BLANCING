# Simulasi Load Balancing i4 dan i7

Project ini berisi simulasi load balancing dengan 4 skenario:

1. i4 + Round Robin
2. i4 + Least Connections
3. i7 + Round Robin
4. i7 + Least Connections

Keterangan:

- i4 = simulasi dengan 4 backend server
- i7 = simulasi dengan 7 backend server
- Round Robin = pembagian request secara bergiliran
- Least Connections = pembagian request ke server dengan koneksi aktif paling sedikit

## Teknologi

- Docker Compose
- Nginx
- Python Flask
- Python requests + ThreadPoolExecutor untuk pengujian paralel

## Struktur File

```text
simulasi_load_balancing_i4_i7/
├── app/
│   └── app.py
├── nginx/
│   ├── i4-roundrobin.conf
│   ├── i4-leastconn.conf
│   ├── i7-roundrobin.conf
│   └── i7-leastconn.conf
├── docker-compose.i4.roundrobin.yml
├── docker-compose.i4.leastconn.yml
├── docker-compose.i7.roundrobin.yml
├── docker-compose.i7.leastconn.yml
├── test.py
├── test_i4_roundrobin.py
├── test_i4_leastconn.py
├── test_i7_roundrobin.py
├── test_i7_leastconn.py
├── run_i4_roundrobin.bat
├── run_i4_leastconn.bat
├── run_i7_roundrobin.bat
├── run_i7_leastconn.bat
├── run_all_tests.py
└── hasil_pengujian/
```

## Cara Menjalankan Manual

### 1. i4 + Round Robin

```bash
docker compose -f docker-compose.i4.roundrobin.yml up --build
```

Buka terminal baru:

```bash
python test_i4_roundrobin.py
```

### 2. i4 + Least Connections

```bash
docker compose -f docker-compose.i4.leastconn.yml up --build
```

Buka terminal baru:

```bash
python test_i4_leastconn.py
```

### 3. i7 + Round Robin

```bash
docker compose -f docker-compose.i7.roundrobin.yml up --build
```

Buka terminal baru:

```bash
python test_i7_roundrobin.py
```

### 4. i7 + Least Connections

```bash
docker compose -f docker-compose.i7.leastconn.yml up --build
```

Buka terminal baru:

```bash
python test_i7_leastconn.py
```

## Cara Paling Mudah di Windows

Klik salah satu file berikut:

```text
run_i4_roundrobin.bat
run_i4_leastconn.bat
run_i7_roundrobin.bat
run_i7_leastconn.bat
```

Setelah container berjalan, buka terminal baru dan jalankan file test sesuai skenario.

## Cara Menjalankan Semua Skenario Otomatis

Jalankan:

```bash
python run_all_tests.py
```

Script ini akan menjalankan semua skenario satu per satu, lalu menyimpan hasilnya di folder:

```text
hasil_pengujian/
```

## Akses Browser

Setelah Docker berjalan, buka:

```text
http://localhost:8085
```

Refresh halaman beberapa kali untuk melihat request berpindah ke server yang berbeda.

## Catatan untuk Laporan

Gunakan screenshot dari:

1. Tampilan browser `http://localhost:8085`
2. Output terminal dari:
   - `python test_i4_roundrobin.py`
   - `python test_i4_leastconn.py`
   - `python test_i7_roundrobin.py`
   - `python test_i7_leastconn.py`
3. File CSV di folder `hasil_pengujian/`
