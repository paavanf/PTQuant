# Pairs Trading Strategy Backtest (Top 1% Quant Project)

## Project Overview
This repository contains a polished, reproducible pairs-trading project designed for a quant portfolio or hackathon submission.
It includes:
- Clean, documented source code
- Synthetic demo data generation (for reproducibility)
- Rigorous statistical procedures (cointegration, rolling hedge ratio)
- A production-style backtest using pandas (easy to extend to Backtrader)
- A multi-page PDF report with figures and results
- Guidance for improvements, risk controls, and deployment

## Repository Structure
```
pairs-trading-backtest/
├── data/                     # CSVs (synthetic demo files created automatically)
├── src/
│   ├── data_generator.py     # reproducible synthetic cointegrated pair
│   ├── pairs_analysis.py     # cointegration test, hedge ratio routines
│   ├── backtest_pd.py        # signal generation + pandas backtesting engine
│   └── run_all.py            # demo runner: produces CSV, plots, summary JSON
├── report_assets/            # assets used in the final report (plots, CSVs)
├── requirements.txt
└── README.md
```

## Quickstart (local)
1. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the demo:
   ```bash
   python src/run_all.py
   ```

3. Generated outputs (plots, CSVs, summary) will be written to `report_assets/`.
   Use those to craft your PDF report or run deeper analyses.

## How this is top-1%
- Statistically principled: cointegration tests + rolling hedge ratio rather than naive spread
- Reproducible: synthetic data generator with seed + clear data contracts (CSV column names)
- Extendable: clear separation between data, analysis, and backtest
- Report-ready: automated generation of figures and JSON summary for reproducible reporting

## Next steps & research ideas
- Add transaction costs, slippage, and realistic execution (limit orders)
- Spread normalization using variance targeting
- Walk-forward cross-validation and parameter optimization
- Extend to portfolios (statistical arbitrage with N assets) using PCA/cointegration clustering

## Contact
For a polished PDF and a GitHub repo ready for submission, contact the author.
