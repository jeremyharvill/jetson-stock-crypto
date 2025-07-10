# signal_reader.py
import json
import os
import time

def read_signal(file_path="signal.json"):
    if not os.path.exists(file_path):
        print("[signal_reader.py] No signal file found.")
        return None

    try:
        with open(file_path, "r") as f:
            signal = json.load(f)
        print(f"[signal_reader.py] Signal received: {signal}")
        return signal
    except Exception as e:
        print(f"[signal_reader.py] Error reading signal: {e}")
        return None

def execute_trade(signal):
    action = signal.get("action")
    ticker = signal.get("ticker")
    confidence = signal.get("confidence")

    print(f"[signal_reader.py] Executing {action} for {ticker} with confidence {confidence:.2f}")
    # Placeholder: Replace with actual broker API call
    # e.g., alpaca.submit_order(...)

def monitor_signals(interval=10):
    print("[signal_reader.py] Monitoring for signals...")
    while True:
        signal = read_signal()
        if signal:
            execute_trade(signal)
            os.remove("signal.json")  # Optional: clean up after execution
        time.sleep(interval)

if __name__ == "__main__":
    monitor_signals()
