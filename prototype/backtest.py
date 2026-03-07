from dataclasses import dataclass
from typing import Dict

@dataclass
class BacktestReport:
    annualized_return: float
    max_drawdown: float
    win_rate: float
    notes: str


def run_backtest(spec) -> BacktestReport:
    # stubbed metrics
    return BacktestReport(
        annualized_return=0.25,
        max_drawdown=0.12,
        win_rate=0.54,
        notes="Stub backtest: replace with real data source + engine",
    )
