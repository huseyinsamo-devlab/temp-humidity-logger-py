# temp-humidity-logger-py

Minimal temperature & humidity logger with CSV storage and a tiny web UI.  
Works on **Raspberry Pi (DHT22/DHT11)** or on **any PC (mock mode)**.

---

## 🚀 Quick Start

```bash
# (Optional) create virtual environment
python -m venv .venv && . .venv/Scripts/activate  # Windows
# python3 -m venv .venv && source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Mock mode (PC): default TH_MOCK=1
python -m thlogger.app

# On Raspberry Pi (real sensor):
# export TH_MOCK=0
# pip install Adafruit_DHT
# python -m thlogger.app
