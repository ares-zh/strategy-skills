# Strategy Skills Prototype

## Goal
Prototype the end-to-end flow: **strategy input → parse → backtest (stub) → deploy (stub)**.

## Files
- `skill.py`: CLI entry for the skill prototype
- `strategies.py`: strategy DSL + parser
- `backtest.py`: simple backtest stub (placeholder)
- `exchanges.py`: exchange adapter interfaces (Bitget/Hyperliquid)

## Run
```bash
python3 skill.py --prompt "EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
```

## Notes
This is a functional skeleton, not yet connected to real exchange APIs or data sources.
