import pandas as pd
import numpy as np

df = pd.read_csv("data/stock_data_with_indicators.csv")

# Future 5-day return
df["Future_Close"] = df["Close"].shift(-5)

df["Future_Return"] = (
    (df["Future_Close"] - df["Close"])
    / df["Close"]
) * 100

# Buy/Sell/Hold classification
conditions = [
    df["Future_Return"] > 2,
    df["Future_Return"] < -2
]

choices = ["Buy", "Sell"]

df["Signal"] = np.select(
    conditions,
    choices,
    default="Hold"
)

df.to_csv(
    "data/stock_data_ml.csv",
    index=False
)

print(df[["Close","Future_Return","Signal"]].tail())
print("ML dataset created successfully!")