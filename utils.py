import datetime

def ts_to_str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")

def pretty_print(data):
    for k, v in data.items():
        print(f"{k}: {v}")

def rolling_average(values):
    if not values:
        return 0
    return sum(values) / len(values)
