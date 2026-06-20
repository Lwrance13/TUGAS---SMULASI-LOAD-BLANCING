import subprocess
import sys

subprocess.run([
        sys.executable,
        'test.py',
        '--mode',
        'i4 Least Connections',
        '--requests',
        '20',
        '--workers',
        '10',
        '--csv',
        'hasil_pengujian/i4_leastconn.csv'
])
