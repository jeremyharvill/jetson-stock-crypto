# signal_writer.py
import json
import os

def write_signal(signal, file_path="signal.json"):
    try:
        with open(file_path, "w") as f:
            json.dump(signal, f, indent=2)
        print(f"[signal_writer.py] Signal written to {file_path}:")
        print(json.dumps(signal, indent=2))
    except Exception as e:
        print(f"[signal_writer.py] Error writing signal: {e}")
