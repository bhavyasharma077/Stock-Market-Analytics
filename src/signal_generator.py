import pandas as pd

df = pd.read_csv("data/stock_data_ml.csv")

latest = df.iloc[-1]

if latest["RSI"] < 30:
    signal = "BUY"
elif latest["RSI"] > 70:
    signal = "SELL"
else:
    signal = "HOLD"

print("Latest Trading Signal:", signal)