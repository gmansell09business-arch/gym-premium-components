import numpy as np, pandas as pd
from harness import *
rng = np.random.default_rng(1)
idx = pd.date_range("2025-01-01", periods=6000, freq="1h")
c = 60000 * np.exp(np.cumsum(rng.normal(0, 0.006, len(idx))))      # pure random walk
df = pd.DataFrame({"close": c}, index=idx)
print("Random-walk data + null forecaster (expect: IC~0, no trades / no edge):")
report(backtest(df, RandomWalkForecaster()), 24 * 365)
