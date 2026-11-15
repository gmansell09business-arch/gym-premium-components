"""Walk-forward backtest harness for a Kronos-style probabilistic candle forecaster.

Forecaster contract: forecast(history_df, horizon) -> ndarray [n_samples, horizon] of
predicted future CLOSES. The agent turns the sample cloud into a trade decision.
"""
from dataclasses import dataclass
import numpy as np, pandas as pd


class RandomWalkForecaster:
    """Null model: no edge by construction. A strategy that 'wins' with this is a bug."""
    def __init__(self, n=30, seed=0): self.n, self.rng = n, np.random.default_rng(seed)
    def forecast(self, hist, horizon):
        r = np.log(hist.close).diff().dropna().tail(200)
        steps = self.rng.normal(r.mean() * 0, r.std(), (self.n, horizon))
        return hist.close.iloc[-1] * np.exp(steps.cumsum(1))


class KronosForecaster:
    """Real model. Needs: git clone shiyu-coder/Kronos (put on PYTHONPATH), torch, HF access."""
    def __init__(self, model="NeoQuasar/Kronos-small", tok="NeoQuasar/Kronos-Tokenizer-base",
                 device="cpu", n=30, lookback=400):
        from model import Kronos, KronosTokenizer, KronosPredictor  # from the Kronos repo
        self.p = KronosPredictor(Kronos.from_pretrained(model), KronosTokenizer.from_pretrained(tok),
                                 device=device, max_context=512)
        self.n, self.lb = n, lookback
    def forecast(self, hist, horizon):
        h = hist.tail(self.lb)
        freq = pd.infer_freq(h.index[-10:]) or (h.index[-1] - h.index[-2])
        fut = pd.date_range(h.index[-1], periods=horizon + 1, freq=freq)[1:]
        cols = [c for c in ["open", "high", "low", "close", "volume", "amount"] if c in h]
        outs = []
        for _ in range(self.n):  # sample_count=1 per call keeps paths independent
            o = self.p.predict(df=h[cols].reset_index(drop=True), x_timestamp=pd.Series(h.index),
                               y_timestamp=pd.Series(fut), pred_len=horizon, T=1.0, top_p=0.9,
                               sample_count=1, verbose=False)
            outs.append(o["close"].to_numpy())
        return np.array(outs)


@dataclass
class Cfg:
    horizon: int = 6          # bars ahead to forecast
    step: int = 6             # re-decide every `step` bars (non-overlapping trades)
    fee_bps: float = 10       # per side (taker)
    slip_bps: float = 5       # per side
    min_edge_bps: float = 30  # require expected move > round-trip cost + margin
    min_p_up: float = 0.58    # require sample agreement
    warmup: int = 400


def decide(paths, last_close, cfg):
    """Long/flat from the sample cloud. Shorting omitted on purpose (perps add funding/liq risk)."""
    final = paths[:, -1] / last_close - 1
    mu_bps, p_up = final.mean() * 1e4, (final > 0).mean()
    cost = 2 * (cfg.fee_bps + cfg.slip_bps)
    return int(mu_bps > cost + cfg.min_edge_bps and p_up >= cfg.min_p_up), mu_bps, p_up


def backtest(df, fc, cfg=Cfg()):
    rows, cost = [], 2 * (cfg.fee_bps + cfg.slip_bps) / 1e4
    for t in range(cfg.warmup, len(df) - cfg.horizon, cfg.step):
        hist = df.iloc[: t + 1]                       # strictly no lookahead
        pos, mu, pu = decide(fc.forecast(hist, cfg.horizon), hist.close.iloc[-1], cfg)
        realized = df.close.iloc[t + cfg.horizon] / df.close.iloc[t] - 1
        rows.append(dict(t=df.index[t], pos=pos, pred_bps=mu, p_up=pu, real=realized,
                         pnl=pos * (realized - cost), bh=realized))
    return pd.DataFrame(rows)


def report(r, bars_per_year):
    n_tr = int(r.pos.sum())
    ppy = bars_per_year / Cfg.step
    sh = lambda x: x.mean() / x.std() * np.sqrt(ppy) if x.std() > 0 else float("nan")
    # Does the forecast carry information at all? (rank corr of predicted vs realised move)
    ic = r.pred_bps.rank().corr(r.real.rank())
    hit = ((r.pred_bps > 0) == (r.real > 0)).mean()
    print(f"decisions={len(r)} trades={n_tr} | IC={ic:+.3f} dir-hit={hit:.1%}")
    print(f"strategy: total={r.pnl.sum():+.2%} sharpe={sh(r.pnl):+.2f} | buy&hold total={r.bh.sum():+.2%}")
