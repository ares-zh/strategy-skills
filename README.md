# Strategy Skills

**One‑line**: Turn a strategy prompt into backtest → deploy → auto‑execute, with exchange adapters (Bitget / Hyperliquid).

## Why
Traditional strategy trading is fragmented. Strategy Skills makes the path **prompt → backtest → execution** one‑click.

## Features (MVP)
- Strategy prompt parsing (plus file/image input soon)
- Backtest stub (metrics + report)
- Exchange adapter skeleton (Bitget/Hyperliquid)
- Risk controls (planned)

## Quick Start
```bash
cd prototype
python3 skill.py --prompt "EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
```

## Project Docs
- PRD: `PRD.md`
- Overview: `PROJECT_OVERVIEW.md`

## Roadmap
See `../reports/hyperliquid_skill_mvp_roadmap.md` (copied into repo soon).

## Contributing
See `CONTRIBUTING.md`.

## License
MIT
