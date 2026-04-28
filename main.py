import threading
import time
from collector import SystemCollector
from analyzer import Analyzer
from stats import Stats
from config import load_config

class Engine:
    def __init__(self):
        self.cfg = load_config()
        self.collector = SystemCollector(self.cfg)
        self.analyzer = Analyzer(self.cfg)
        self.stats = Stats(self.cfg)
        self.running = False

    def start(self):
        self.running = True
        t1 = threading.Thread(target=self.collect_loop, daemon=True)
        t2 = threading.Thread(target=self.analyze_loop, daemon=True)
        t1.start()
        t2.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print("\n[+] Shutting down cleanly")

    def collect_loop(self):
        while self.running:
            data = self.collector.collect()
            self.stats.add(data)
            time.sleep(self.cfg["interval"])

    def analyze_loop(self):
        while self.running:
            snapshot = self.stats.snapshot()
            alerts = self.analyzer.run(snapshot)
            for alert in alerts:
                print("[ALERT]", alert)
            time.sleep(self.cfg["analysis_interval"])


if __name__ == "__main__":
    Engine().start()
