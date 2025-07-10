# engineered.py
import pandas as pd

def add_engineered_features(df, lag_days=3, corr_window=5):
    df = df.copy()

    # Percent Change
    df["Pct_Change"] = df["Close"].pct_change()

    # Volatility (Rolling Standard Deviation)
    df["Volatility"] = df["Close"].rolling(window=10).std()

    # Lag Features
    for i in range(1, lag_days + 1):
        df[f"Close_Lag_{i}"] = df["Close"].shift(i)
        df[f"Volume_Lag_{i}"] = df["Volume"].shift(i)

    # Rolling Correlation with Volume
    df["Corr_Close_Volume"] = df["Close"].rolling(window=corr_window).corr(df["Volume"])

    # Rolling Mean of Volume
    df["Volume_Mean"] = df["Volume"].rolling(window=10).mean()

    return df
