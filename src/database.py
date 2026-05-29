import yfinance as yf
import pandas as pd

stock = "RELIANCE.NS"

data = yf.download(
    stock,
    start="2020-01-01",
    end="2025-01-01"
)

data.to_csv("data/stock_data.csv")

print("Stock data saved successfully")