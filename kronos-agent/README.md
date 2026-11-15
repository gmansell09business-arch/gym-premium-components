# Kronos trading-agent exploration

Kronos = open-source decoder-only foundation model for candlesticks (shiyu-coder/Kronos, AAAI 2026).
OHLCV(+amount) -> hierarchical discrete tokens -> autoregressive transformer; pretrained on 12 **billion**
K-lines from 45+ exchanges. Weights on HF: Kronos-mini (4.1M, ctx 2048), small (24.7M, ctx 512),
base (102M, ctx 512). Large (499M) is not released. Supports fine-tuning (scripts in repo).

## What it is / isn't
- It is a *probabilistic candle simulator*: sample N future paths -> distribution of returns/vol.
- It is not a trading agent. Everything between forecast and fill (sizing, costs, risk) is on us.
- Short-horizon crypto is near-efficient; after ~20-30 bps round-trip costs, a tiny IC is worth nothing.
- The viral dashboards (screenshots) show "SIMULATED"/paper numbers; profit claims are unverified.

## Pipeline
1. Data: public klines (Binance/other) 1h or 5m, OHLCV + quote volume as `amount`. Keep a 12+ month holdout.
2. Forecast: N=30-100 sampled paths, horizon H (e.g. 6 bars), lookback <= 512.
3. Signal: long/flat if mean move > round-trip cost + margin AND P(up) >= threshold (harness.decide).
4. Evaluate walk-forward, no lookahead: IC, direction hit-rate, net Sharpe vs buy&hold, drawdown.
5. Gate: only if IC is stably > 0 across regimes/assets/time splits do we go to paper trading (weeks),
   then tiny live size with hard limits (max position, daily loss stop, kill switch).
6. Then try: fine-tune on target asset; use vol forecast for sizing instead of direction; ensemble with simple baselines.

## Run
- Offline sanity (done): `python3 demo_offline.py` -> null forecaster on random-walk data loses ~costs
  (IC -0.006, hit 49%). Any "edge" the harness shows on random data = bug.
- Real: `git clone https://github.com/shiyu-coder/Kronos`, `pip install torch -r Kronos/requirements.txt`,
  put Kronos on PYTHONPATH, fetch klines to a DataFrame (DatetimeIndex; open/high/low/close/volume/amount),
  `backtest(df, KronosForecaster(device="cuda"))`. CPU is slow: 30 samples x ~900 decisions.
- This sandbox blocks huggingface.co and Binance, so KronosForecaster is written against the README API
  but is UNTESTED.

## Not built (deliberately)
Live order execution. Add only after step 5 passes.
