from dataclasses import dataclass
from typing import List
import ccxt
import time

@dataclass
class BacktestReport:
    annualized_return: float
    max_drawdown: float
    win_rate: float
    trades: int
    notes: str


def _sma(values: List[float], period: int) -> List[float]:
    out = [None] * len(values)
    s = 0.0
    for i, v in enumerate(values):
        s += v
        if i >= period:
            s -= values[i - period]
        if i >= period - 1:
            out[i] = s / period
    return out


def _max_drawdown(equity: List[float]) -> float:
    peak = equity[0]
    max_dd = 0.0
    for v in equity:
        if v > peak:
            peak = v
        dd = (peak - v) / peak if peak else 0
        if dd > max_dd:
            max_dd = dd
    return max_dd


def run_backtest(spec, limit: int = 500) -> BacktestReport:
    """Simple SMA crossover backtest using OHLCV from Binance via CCXT.
    - Uses close prices
    - Long-only by default
    """
    exchange = ccxt.binance({"enableRateLimit": True})
    ohlcv = exchange.fetch_ohlcv(spec.symbol.replace("USDT", "/USDT"), timeframe=spec.timeframe, limit=limit)
    closes = [c[4] for c in ohlcv]

    fast = _sma(closes, 20)
    slow = _sma(closes, 50)

    position = 0
    entry = 0.0
    equity = [1.0]
    wins = 0
    trades = 0

    for i in range(len(closes)):
        if fast[i] is None or slow[i] is None:
            equity.append(equity[-1])
            continue

        # entry
        if position == 0 and fast[i] > slow[i]:
            position = 1
            entry = closes[i]
            trades += 1

        # exit
        if position == 1 and fast[i] < slow[i]:
            ret = (closes[i] - entry) / entry
            if ret > 0:
                wins += 1
            equity.append(equity[-1] * (1 + ret))
            position = 0
            entry = 0.0
            continue

        equity.append(equity[-1])

    total_return = equity[-1] - 1.0
    years = (len(closes) * _tf_to_days(spec.timeframe)) / 365.0
    annualized = (1 + total_return) ** (1 / years) - 1 if years > 0 else 0
    max_dd = _max_drawdown(equity)
    win_rate = wins / trades if trades else 0

    return BacktestReport(
        annualized_return=annualized,
        max_drawdown=max_dd,
        win_rate=win_rate,
        trades=trades,
        notes="Simple SMA(20/50) backtest using Binance OHLCV",
    ), equity


def _tf_to_days(tf: str) -> float:
    if tf.endswith("m"):
        return int(tf[:-1]) / (60 * 24)
    if tf.endswith("h"):
        return int(tf[:-1]) / 24
    if tf.endswith("d"):
        return int(tf[:-1])
    return 1 / 24
