from collections import deque

class Stats:
    def __init__(self, cfg):
        self.history = deque(maxlen=cfg["history_size"])

    def add(self, data):
        self.history.append(data)

    def snapshot(self):
        return list(self.history)

    def clear(self):
        self.history.clear()

    def size(self):
        return len(self.history)
