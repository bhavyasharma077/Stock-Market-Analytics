import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/stock_data_with_indicators.csv")

plt.figure(figsize=(12,6))
plt.plot(df["Close"])

plt.title("Reliance Stock Price Trend")
plt.xlabel("Trading Days")
plt.ylabel("Closing Price")

plt.grid(True)

# Save image
plt.savefig("visualization/stock_price_trend.png")

# Show graph
plt.show()

print("Chart saved successfully!")