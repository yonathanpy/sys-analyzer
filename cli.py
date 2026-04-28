import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description="sys-analyzer CLI")
    parser.add_argument("--interval", type=int, help="Collection interval")
    parser.add_argument("--analysis-interval", type=int, help="Analysis interval")
    parser.add_argument("--config", type=str, help="Path to config file")
    return parser.parse_args()


def apply_cli_overrides(cfg, args):
    if args.interval:
        cfg["interval"] = args.interval
    if args.analysis_interval:
        cfg["analysis_interval"] = args.analysis_interval
    return cfg


def export_config(cfg, path="config_dump.json"):
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)
