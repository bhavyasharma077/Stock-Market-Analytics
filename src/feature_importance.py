import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/stock_data_ml.csv")
df = df.dropna()

X = df[[
    "RSI",
    "MACD",
    "BB_Upper",
    "BB_Lower",
    "Volume"
]]

y = df["Signal"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(X.columns, importance)

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.tight_layout()

plt.savefig(
    "visualization/feature_importance.png"
)

plt.show()

print("Feature importance chart saved.")