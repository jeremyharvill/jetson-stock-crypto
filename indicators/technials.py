# technicals.py
import pandas as pd

def add_technical_indicators(df, sma_period=14, ema_period=14, rsi_period=14):
    df = df.copy()

    # Simple Moving Average (SMA)
    df["SMA"] = df["Close"].rolling(window=sma_period).mean()

    # Exponential Moving Average (EMA)
    df["EMA"] = df["Close"].ewm(span=ema_period, adjust=False).mean()

    # Relative Strength Index (RSI)
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=rsi_period).mean()
    avg_loss = loss.rolling(window=rsi_period).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # MACD (Moving Average Convergence Divergence)
    ema_fast = df["Close"].ewm(span=12, adjust=False).mean()
    ema_slow = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema_fast - ema_slow
    df["MACD_Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    return df
