import json
import os

DEFAULT_CONFIG = {
    "interval": 2,
    "analysis_interval": 5,
    "cpu_threshold": 85,
    "memory_threshold": 80,
    "history_size": 50
}

def load_config(path=None):
    if path and os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    return DEFAULT_CONFIG.copy()


def save_config(cfg, path="config.json"):
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)


def validate_config(cfg):
    assert cfg["interval"] > 0
    assert cfg["analysis_interval"] > 0
    assert 0 < cfg["cpu_threshold"] <= 100
    assert 0 < cfg["memory_threshold"] <= 100
