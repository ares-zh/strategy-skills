# Risk Guardrails

## Defaults
- **Explicit confirmation** required before any live order
- **Smallest size** on first run
- **Max position** and **daily loss cap** enforced (from config)

## Config knobs
Set via `scripts/config_wizard.sh` → `~/.strategy-skills.env`
- `MAX_POSITION`
- `DAILY_LOSS`
- `REVIEW_TIME`

## Recommended limits
- Start with small size (e.g., $50–$100)
- Daily loss cap ≤ 1–2% of account

## Failure behavior
- If exchange API fails, no retry‑by‑default for live orders
- All errors logged; no silent execution
