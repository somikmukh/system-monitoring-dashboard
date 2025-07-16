from fastapi import FastAPI, WebSocket
import psutil
import asyncio
import sqlite3
import datetime

app = FastAPI()

conn = sqlite3.connect("metrics.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    disk REAL
)
""")

def store_metrics(data):
    now = datetime.datetime.now().isoformat()
    cursor.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)",
                   (now, data["cpu"], data["memory"], data["disk"]))
    conn.commit()

def alert_if_high(data):
    if data["cpu"] > 90:
        print("⚠️ High CPU usage detected!")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = {
            "cpu": psutil.cpu_percent(percpu=False),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "net": psutil.net_io_counters(pernic=False)._asdict()
        }
        alert_if_high(data)
        store_metrics(data)
        await websocket.send_json(data)
        await asyncio.sleep(1)