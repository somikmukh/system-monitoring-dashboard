import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("metrics.db")
df = pd.read_sql("SELECT * FROM metrics", conn, parse_dates=["timestamp"])
df.set_index("timestamp").plot()
plt.title("System Metrics Over Time")
plt.xlabel("Time")
plt.ylabel("Usage %")
plt.savefig("daily_report.png")