@echo off
echo ===============================================
echo Menjalankan skenario: i4 Least Connections
echo ===============================================
echo.
echo Menghentikan container skenario lain jika masih berjalan...
docker compose -f docker-compose.i4.roundrobin.yml down
docker compose -f docker-compose.i4.leastconn.yml down
docker compose -f docker-compose.i7.roundrobin.yml down
docker compose -f docker-compose.i7.leastconn.yml down
echo.
echo Menjalankan Docker Compose...
docker compose -f docker-compose.i4.leastconn.yml up --build
pause
