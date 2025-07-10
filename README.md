# jetson-stock-crypto
# Jetson Crypto Pipeline

This project uses Jetson Nano devices to analyze cryptocurrency data and execute trades automatically using machine learning.

## Setup
1. Flash Jetson Nano with JetPack
2. Clone repository
3. Run `main.py` to start analysis
4. View dashboard at `http://<jetson-ip>:5000`

## Modules
- `trainer.py`: ML training
- `signal_writer.py`: Signal generation
- `signal_reader.py`: Trade execution
- `app.py`: Dashboard
