# 🖥️ Python System Monitoring Dashboard

A real-time system resource monitor built entirely with Python + FastAPI + Chart.js — no Grafana or Prometheus needed.
Special thanks and credits to Abdul Ahad for the documentation.

## 📊 Features

- Live CPU, Memory, and Disk usage
- Real-time chart with Chart.js
- Data storage using SQLite
- Daily reports with pandas + matplotlib
- Simple voice alerts and alerts on high CPU
- Optional EXE bundling with PyInstaller

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/system-monitor.git
cd system-monitor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn server:app --reload
```

### 4. View the dashboard
```bash
python -m http.server 8080
```
Then open http://localhost:8080/index.html

### 5. Generate report manually (optional)
```bash
python generate_report.py
```
