📈 Stock Market Intelligent Analytics Platform

An end-to-end stock market analytics platform built using Python, MySQL, and Machine Learning. The project collects historical stock data, calculates technical indicators, generates trading signals, performs predictive analysis, and stores insights in a relational database.

---

🚀 Features

- Historical stock data collection using Yahoo Finance
- Technical indicator calculation:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
- Trend visualization and analysis
- Feature importance analysis using Random Forest
- Correlation heatmap generation
- Buy / Sell / Hold signal generation
- Machine Learning based trend classification
- MySQL database integration
- Automated storage of trading signals
- Model persistence using Joblib

---

🛠️ Tech Stack

Programming

- Python

Data Analysis

- Pandas
- NumPy

Machine Learning

- Scikit-Learn
- Random Forest Classifier

Visualization

- Matplotlib

Financial Analysis

- yFinance
- ta (Technical Analysis Library)

Database

- MySQL
- MySQL Connector

Version Control

- Git
- GitHub

---

📂 Project Structure

Stock-Market-Analytics/
│
├── data/
│   ├── stock_data.csv
│   ├── stock_data_with_indicators.csv
│   └── stock_data_ml.csv
│
├── sql/
│
├── src/
│   ├── database.py
│   ├── indicators.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── feature_importance.py
│   ├── correlation_heatmap.py
│   ├── signal_generator.py
│   ├── mysql_integration.py
│   └── save_model.py
│
├── visualization/
│   ├── stock_price_trend.png
│   ├── feature_importance.png
│   └── correlation_heatmap.png
│
├── model.pkl
├── requirements.txt
├── README.md
└── main.py

---

📊 Machine Learning Pipeline

1. Collect historical stock data
2. Calculate technical indicators
3. Generate Buy/Sell/Hold labels
4. Train Random Forest classifier
5. Evaluate model performance
6. Generate trading signals
7. Store signals in MySQL
8. Save trained model for future predictions

---

📈 Visualizations

Stock Price Trend

Displays historical stock movement and trend behavior.

Feature Importance Analysis

Identifies the most influential indicators affecting model predictions.

Correlation Heatmap

Shows relationships between stock price, technical indicators, and volume.

---

🗄️ Database Integration

The project uses MySQL to store generated trading signals.

Table: stock_signals

Column| Description
id| Unique signal identifier
close_price| Latest closing price
rsi| Current RSI value
signal_type| BUY / SELL / HOLD

---

▶️ How to Run

Install dependencies:

pip install -r requirements.txt

Collect stock data:

python src/database.py

Calculate indicators:

python src/indicators.py

Prepare ML dataset:

python src/preprocessing.py

Train model:

python src/model.py

Generate signal:

python src/signal_generator.py

Store signal in MySQL:

python src/mysql_integration.py

---

🎯 Key Learning Outcomes

- Financial data analysis
- Technical indicator engineering
- Machine Learning classification
- Data visualization
- Database management
- Model deployment concepts
- Git and GitHub workflow

---

🔮 Future Improvements

- Streamlit dashboard
- Portfolio analytics
- Volatility prediction model
- Real-time stock monitoring
- Automated daily signal updates
- Advanced ensemble models

---

👨‍💻 Author

Bhavya Sharma

Stock Market Intelligent Analytics Platform developed as a data analytics and machine learning project demonstrating financial analysis, predictive modeling, and database integration.

