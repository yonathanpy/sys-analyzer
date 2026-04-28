import psutil
import time

class SystemCollector:
    def __init__(self, cfg):
        self.cfg = cfg

    def collect(self):
        data = {
            "timestamp": time.time(),
            "cpu": psutil.cpu_percent(interval=None),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent,
            "process_count": len(psutil.pids())
        }
        return data

    def collect_processes(self):
        result = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                result.append(proc.info)
            except Exception:
                continue
        return result
