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
pip install -r requirements.txt
# set Bitget demo API keys
export BITGET_API_KEY=...
export BITGET_API_SECRET=...
export BITGET_API_PASSPHRASE=...

python3 skill.py --prompt "EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%" --exchange bitget --dry-run

# file input
python3 skill.py --file examples/strategy.json --exchange bitget --dry-run

# market buy by cost (USDT amount)
python3 skill.py --prompt "..." --exchange bitget --order-type market --cost 20 --dry-run

# limit buy
python3 skill.py --prompt "..." --exchange bitget --order-type limit --price 65000 --dry-run

# hyperliquid market
python3 skill.py --prompt "..." --exchange hyperliquid --order-type market --dry-run

# hyperliquid limit
python3 skill.py --prompt "..." --exchange hyperliquid --order-type limit --price 65000 --dry-run
```

## Notes
Backtest fetches OHLCV from Binance via CCXT (no API key required).
Execution supports Bitget adapter (dry-run by default). Market buy can use `--cost`.
