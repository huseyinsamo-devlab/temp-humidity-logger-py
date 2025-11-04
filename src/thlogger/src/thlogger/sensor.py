from .hw import DHTBackend

class THSensor:
    def __init__(self, pin=4, sensor="DHT22"):
        self._backend = DHTBackend(pin=pin, sensor=sensor)

    def read(self):
        # (temperature °C, humidity %)
        return self._backend.read()
