"""Run demo backtest: generate synthetic cointegrated pair, produce CSVs, plots and summary."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_cointegrated_pair
from pairs_analysis import cointegration_test, rolling_hedge_ratio
from backtest_pd import zscore, generate_signals, backtest_pair
import json
from datetime import datetime

BASE = Path(__file__).resolve().parents[1]
data_dir = BASE / 'data'
out_dir = BASE / 'report_assets'
out_dir.mkdir(exist_ok=True)

s1, s2 = generate_cointegrated_pair(n_days=1000, seed=123, beta=1.25, sigma_noise=0.6)
s1.to_csv(data_dir / 'stockA.csv')
s2.to_csv(data_dir / 'stockB.csv')

prices_a = pd.read_csv(data_dir / 'stockA.csv', index_col=0, parse_dates=True)
prices_b = pd.read_csv(data_dir / 'stockB.csv', index_col=0, parse_dates=True)

score, pvalue = cointegration_test(prices_a['Close'], prices_b['Close'])

hedge = rolling_hedge_ratio(prices_a['Close'], prices_b['Close'], window=60)

spread = prices_a['Close'] - hedge * prices_b['Close']
spread_z = zscore(spread, window=60)

signals = generate_signals(spread_z, entry_z=2.0, exit_z=0.0)
stats = backtest_pair(prices_a, prices_b, hedge, signals)

prices_a.to_csv(out_dir / 'stockA_used.csv')
prices_b.to_csv(out_dir / 'stockB_used.csv')
spread.to_csv(out_dir / 'spread_series.csv')
spread_z.to_csv(out_dir / 'spread_z.csv')
signals.to_csv(out_dir / 'signals.csv')

plt.figure(figsize=(10,4))
plt.plot(prices_a['Close'], label='Stock A')
plt.plot(prices_b['Close'], label='Stock B')
plt.title('Price Series (synthetic)')
plt.legend()
plt.tight_layout()
plt.savefig(out_dir / 'prices.png')
plt.close()

plt.figure(figsize=(10,4))
plt.plot(spread, label='Spread')
plt.plot(spread.rolling(60).mean(), label='Rolling mean')
plt.title('Spread + Rolling Mean')
plt.legend()
plt.tight_layout()
plt.savefig(out_dir / 'spread.png')
plt.close()

plt.figure(figsize=(10,4))
plt.plot(spread_z, label='z-score')
plt.axhline(2.0, linestyle='--')
plt.axhline(-2.0, linestyle='--')
plt.title('Spread z-score (entry/exit levels)')
plt.tight_layout()
plt.savefig(out_dir / 'zscore.png')
plt.close()

plt.figure(figsize=(10,4))
stats['cum_ret_series'].plot()
plt.title('Cumulative Returns (strategy units)')
plt.tight_layout()
plt.savefig(out_dir / 'cum_returns.png')
plt.close()

summary = {
    'cointegration_pvalue': float(pvalue),
    'cointegration_score': float(score),
    'total_return': float(stats['total_return']),
    'annual_return': float(stats['annual_return']),
    'sharpe': float(stats['sharpe']) if not pd.isna(stats['sharpe']) else None,
    'max_drawdown': float(stats['max_drawdown'])
}
with open(out_dir / 'summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print('Demo run complete. Outputs written to', out_dir)
