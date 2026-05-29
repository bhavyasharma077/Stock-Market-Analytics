import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhavya@240004012",
    database="stock_analytics"
)

cursor = conn.cursor()

df = pd.read_csv("data/stock_data_ml.csv")

latest = df.iloc[-1]

if latest["RSI"] < 30:
    signal = "BUY"
elif latest["RSI"] > 70:
    signal = "SELL"
else:
    signal = "HOLD"

query = """
INSERT INTO stock_signals
(close_price, rsi, signal_type)
VALUES (%s, %s, %s)
"""

values = (
    float(latest["Close"]),
    float(latest["RSI"]),
    signal
)

cursor.execute(query, values)

conn.commit()

print("Signal stored successfully!")

cursor.close()
conn.close()