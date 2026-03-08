---
name: strategy-skills
description: End-to-end strategy execution for OpenClaw. Parse prompt/file/image → backtest → deploy → execute → receipt. Supports Bitget and Hyperliquid. Includes risk guards and reporting.
---

# Strategy Skills

## What it does
Turn a strategy idea into a runnable pipeline: parse → backtest → deploy → execute → receipt.

## Inputs
- Strategy prompt / file / image
- Exchange: Bitget / Hyperliquid
- Risk: max size, stop loss, daily loss cap

## Safety
- Auto-exec requires explicit confirmation
- Smallest size on first run

## Quick start
- Run config wizard: `scripts/config_wizard.sh`
- Use in OpenClaw: "Use Strategy Skills: EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
