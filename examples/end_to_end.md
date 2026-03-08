# End‑to‑End Demo (Prompt → Backtest → Execute)

## 1) Configure
```bash
./scripts/config_wizard.sh
```

## 2) Run with a prompt
```
Use Strategy Skills: EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%
```

## 3) Expected outputs
- Backtest metrics + equity curve
- Confirmation request for live execution
- Standardized receipt after order status fetch

## 4) Optional inputs
- Strategy JSON file: `--file examples/strategy.json`
- Screenshot OCR: `--image examples/strategy.png`

## 5) Reports
- `backtest_equity.png`, `backtest_report.html`
- `trade_pnl.png`, `trade_review.html`
