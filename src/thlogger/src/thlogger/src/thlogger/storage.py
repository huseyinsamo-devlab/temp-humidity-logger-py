import csv, os, time
from pathlib import Path

DATA_DIR = Path(os.getenv("TH_DATA_DIR", "data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)
CSV_FILE = DATA_DIR / "readings.csv"

def append_reading(temp_c: float, hum_pct: float):
    new_file = not CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "temperature_c", "humidity_pct"])
        w.writerow([int(time.time()), temp_c, hum_pct])

def read_last(n: int = 50):
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows[-n:]
