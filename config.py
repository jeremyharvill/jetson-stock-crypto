# config.py

# Top 32 crypto tickers for ensemble prediction
TICKERS = [
    "BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD",
    "XRP-USD", "DOGE-USD", "TON-USD", "AVAX-USD", "DOT-USD",
    "TRX-USD", "LINK-USD", "MATIC-USD", "XLM-USD", "NEAR-USD",
    "UNI-USD", "ICP-USD", "LTC-USD", "APT-USD", "BCH-USD",
    "FIL-USD", "INJ-USD", "ETC-USD", "RNDR-USD", "DAI-USD",
    "XMR-USD", "KAS-USD", "FET-USD", "TAO-USD", "SUI-USD",
    "LDO-USD", "HBAR-USD"
]

# Other configuration constants
SIGNAL_THRESHOLD = 0.85
DATA_START = "2023-01-01"
DATA_END = "2024-01-01"
MODEL_TYPE = "regression"  # or "classification"
