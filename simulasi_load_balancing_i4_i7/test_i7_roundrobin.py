import subprocess
import sys

subprocess.run([
        sys.executable,
        'test.py',
        '--mode',
        'i7 Round Robin',
        '--requests',
        '28',
        '--workers',
        '14',
        '--csv',
        'hasil_pengujian/i7_roundrobin.csv'
])
