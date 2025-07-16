import psutil

def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "net": psutil.net_io_counters(pernic=False)._asdict()
    }

if __name__ == "__main__":
    print(get_metrics())