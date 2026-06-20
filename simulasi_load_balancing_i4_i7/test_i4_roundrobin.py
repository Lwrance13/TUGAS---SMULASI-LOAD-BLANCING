import subprocess
import sys

subprocess.run([
        sys.executable,
        'test.py',
        '--mode',
        'i4 Round Robin',
        '--requests',
        '20',
        '--workers',
        '10',
        '--csv',
        'hasil_pengujian/i4_roundrobin.csv'
])
