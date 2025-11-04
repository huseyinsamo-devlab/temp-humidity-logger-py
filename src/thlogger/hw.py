import os, time, random

USE_MOCK = os.getenv("TH_MOCK", "1") == "1"  # Varsayılan mock: PC'de çalışsın

class DHTBackend:
    def __init__(self, pin=4, sensor="DHT22"):
        self.pin = pin
        self.sensor = sensor
        if not USE_MOCK:
            try:
                import Adafruit_DHT  # type: ignore
                self._lib = Adafruit_DHT
                self._kind = self._lib.DHT22 if sensor == "DHT22" else self._lib.DHT11
            except Exception as e:
                raise RuntimeError(f"Adafruit_DHT bulunamadı: {e}")

    def read(self):
        if USE_MOCK:
            # Demo verisi: 22–28°C, 35–60% nem
            t = round(random.uniform(22.0, 28.0), 1)
            h = round(random.uniform(35.0, 60.0), 1)
            time.sleep(0.3)
            return t, h
        humidity, temperature = self._lib.read_retry(self._kind, self.pin)
        if humidity is None or temperature is None:
            raise RuntimeError("DHT okuma hatası")
        return round(float(temperature), 1), round(float(humidity), 1)
