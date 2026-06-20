from flask import Flask, jsonify
import os
import socket
import time
from datetime import datetime

app = Flask(__name__)

SERVER_NAME = os.environ.get("SERVER_NAME", socket.gethostname())
SERVER_GROUP = os.environ.get("SERVER_GROUP", "unknown")
SERVER_COLOR = os.environ.get("SERVER_COLOR", "#00d4ff")
PROCESS_DELAY = float(os.environ.get("PROCESS_DELAY", "0.1"))

@app.route("/")
def index():
    time.sleep(PROCESS_DELAY)

    hostname = socket.gethostname()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Load Balancing Monitor</title>
    <style>
        * {{
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }}
        body {{
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at top, #1f3b57, #07111f);
            color: #ffffff;
        }}
        .card {{
            width: 440px;
            padding: 28px;
            border-radius: 18px;
            background: rgba(17, 34, 52, 0.94);
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        h1 {{
            margin: 0;
            font-size: 24px;
            text-align: center;
            letter-spacing: 1px;
        }}
        .subtitle {{
            text-align: center;
            margin: 8px 0 24px;
            color: #9fb3c8;
            font-size: 13px;
        }}
        .box {{
            padding: 18px;
            margin-top: 14px;
            border-radius: 12px;
            background: rgba(8, 19, 33, 0.85);
            border-left: 5px solid {SERVER_COLOR};
        }}
        .label {{
            font-size: 12px;
            color: #8fa8bd;
            text-transform: uppercase;
            margin-bottom: 6px;
        }}
        .value {{
            font-size: 19px;
            font-weight: bold;
            color: {SERVER_COLOR};
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #8fa8bd;
            font-size: 12px;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>LOAD BALANCING MONITOR</h1>
        <div class="subtitle">Simulasi {SERVER_GROUP} - Nginx + Docker + Flask</div>

        <div class="box">
            <div class="label">Request diproses oleh</div>
            <div class="value">{SERVER_NAME}</div>
        </div>

        <div class="box">
            <div class="label">Container Hostname</div>
            <div class="value">{hostname}</div>
        </div>

        <div class="box">
            <div class="label">Response Delay</div>
            <div class="value">{PROCESS_DELAY} Seconds</div>
        </div>

        <div class="footer">
            Waktu respons: {timestamp}<br>
            Refresh halaman untuk melihat perpindahan server.
        </div>
    </div>
</body>
</html>
"""

@app.route("/api")
def api():
    time.sleep(PROCESS_DELAY)
    return jsonify({
        "server_name": SERVER_NAME,
        "server_group": SERVER_GROUP,
        "hostname": socket.gethostname(),
        "delay_seconds": PROCESS_DELAY,
        "timestamp": datetime.now().isoformat(timespec="seconds")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
