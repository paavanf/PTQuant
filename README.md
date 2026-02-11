# 📊 Statistical Arbitrage: Pairs Trading Strategy Backtest

## 🚀 Overview

This project implements a **quantitative pairs trading strategy** using statistical arbitrage principles.
The model identifies cointegrated stock pairs, generates trading signals based on spread deviation, and evaluates performance through backtesting.

Designed as a **quant finance portfolio project**, this demonstrates real-world trading strategy development used in hedge funds and proprietary trading firms.

---

## 🧠 Strategy Logic

### 1. Cointegration Testing

* Uses Engle-Granger cointegration test
* Identifies mean-reverting stock pairs
* Ensures statistical relationship exists

### 2. Spread Modeling

* Rolling hedge ratio using OLS regression
* Spread = Stock A − β × Stock B
* Z-score normalization

### 3. Trading Signals

| Condition       | Action       |
| --------------- | ------------ |
| Z-score > +2    | Short spread |
| Z-score < −2    | Long spread  |
| Reverts to mean | Exit         |

### 4. Backtesting Engine

* Rolling window analysis
* Cumulative returns tracking
* Sharpe ratio & drawdown calculation

---

## 📈 Performance Metrics

* Total Return
* Annualized Return
* Sharpe Ratio
* Maximum Drawdown
* Cointegration p-value

---

## 🛠 Tech Stack

* Python
* Pandas & NumPy
* Statsmodels
* Matplotlib
* Quantitative Finance Methods

---

## 📊 Generated Outputs

* Spread & Z-score charts
* Trading signals
* Cumulative returns curve
* Automated PDF performance report

---

## 📂 Project Structure

```
pairs-trading-backtest/
│
├── src/                # Strategy & backtest code
├── data/               # Input price data
├── report_assets/      # Generated charts & metrics
├── Pairs_Trading_Report.pdf
└── README.md
```

---

## 💡 Future Improvements

* Transaction cost modeling
* Live market data integration (NSE/NYSE)
* Portfolio-level statistical arbitrage
* Machine learning-based pair selection
* Deployment for live trading

---

## 👨‍💻 Author

**Paavan Fatepuria**
Aspiring Quant Developer | Data Science | Trading Systems

---

## ⭐ If you found this interesting

Star the repo — helps visibility!
