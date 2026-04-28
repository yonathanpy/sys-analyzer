class Analyzer:
    def __init__(self, cfg):
        self.cfg = cfg

    def run(self, snapshot):
        alerts = []
        if not snapshot:
            return alerts

        avg_cpu = self._avg(snapshot, "cpu")
        avg_mem = self._avg(snapshot, "memory")

        if avg_cpu > self.cfg["cpu_threshold"]:
            alerts.append(f"High CPU usage detected: {avg_cpu:.2f}%")

        if avg_mem > self.cfg["memory_threshold"]:
            alerts.append(f"High memory usage detected: {avg_mem:.2f}%")

        spikes = self._detect_spikes(snapshot)
        alerts.extend(spikes)

        return alerts

    def _avg(self, data, key):
        return sum(d[key] for d in data) / len(data)

    def _detect_spikes(self, data):
        alerts = []
        for i in range(1, len(data)):
            if data[i]["cpu"] - data[i-1]["cpu"] > 40:
                alerts.append("CPU spike detected")
        return alerts
