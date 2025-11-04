from flask import Flask, jsonify, render_template_string, request
from .sensor import THSensor
from .storage import append_reading, read_last

app = Flask(__name__)
sensor = THSensor()  # TH_MOCK=1 ise mock, aksi donanım

INDEX_HTML = """
<!doctype html>
<title>TH Logger</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<h1>Temperature & Humidity Logger</h1>
<p><button onclick="fetch('/api/sample',{method:'POST'}).then(()=>location.reload())">Yeni Örnek Al</button></p>
<table border="1" cellpadding="6">
<tr><th>#</th><th>Zaman (epoch)</th><th>Sıcaklık (°C)</th><th>Nem (%)</th></tr>
{% for i,row in enumerate(data) %}
<tr>
  <td>{{ i+1 }}</td>
  <td>{{ row['timestamp'] }}</td>
  <td>{{ row['temperature_c'] }}</td>
  <td>{{ row['humidity_pct'] }}</td>
</tr>
{% endfor %}
</table>
<p><small>POST /api/sample ile yeni okuma alınır · GET /api/last ile son veriler JSON döner</small></p>
"""

@app.get("/")
def index():
    data = read_last(50)
    return render_template_string(INDEX_HTML, data=data)

@app.get("/api/last")
def api_last():
    return jsonify(read_last(50))

@app.post("/api/sample")
def api_sample():
    t, h = sensor.read()
    append_reading(t, h)
    return jsonify({"ok": True, "temperature_c": t, "humidity_pct": h})

def main():
    # İlk örnek veri yoksa bir okuma almayı deneyebiliriz (opsiyonel)
    try:
        t, h = sensor.read()
        append_reading(t, h)
    except Exception:
        pass
    app.run(host="127.0.0.1", port=8000, debug=False)

if __name__ == "__main__":
    main()
