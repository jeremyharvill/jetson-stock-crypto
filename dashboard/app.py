# app.py
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signal")
def view_signal():
    try:
        with open("signal.json", "r") as f:
            signal = json.load(f)
        return jsonify(signal)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/trigger", methods=["POST"])
def trigger_action():
    action = request.json.get("action")
    ticker = request.json.get("ticker")
    confidence = request.json.get("confidence")

    signal = {
        "action": action,
        "ticker": ticker,
        "confidence": confidence
    }

    try:
        with open("signal.json", "w") as f:
            json.dump(signal, f, indent=2)
        return jsonify({"status": "Signal triggered", "signal": signal})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
