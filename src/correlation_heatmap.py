import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/stock_data_ml.csv")

df = df[[
    "Close",
    "RSI",
    "MACD",
    "BB_Upper",
    "BB_Lower",
    "Volume"
]]

corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("visualization/correlation_heatmap.png")

plt.show()

print("Correlation heatmap saved successfully!")