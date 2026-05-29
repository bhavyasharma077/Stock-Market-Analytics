import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/stock_data_ml.csv")
df = df.dropna()

X = df[["RSI","MACD","BB_Upper","BB_Lower","Volume"]]
y = df["Signal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("Model saved successfully!")