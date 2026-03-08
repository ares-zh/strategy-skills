# Logs & Troubleshooting

## Where to look
- OpenClaw logs: `~/.openclaw/logs/` (agent + tool output)
- Strategy‑skills outputs: `~/.strategy-skills/reports/YYYY-MM-DD/`

## Common issues
1) **No report generated**
   - Daily review only runs at `REVIEW_TIME` (default 20:00)
   - Ensure `~/.strategy-skills/trades.csv` exists

2) **OCR errors**
   - Install tesseract: `scripts/install_ocr.sh`

3) **Exchange order failures**
   - Check API keys in `~/.strategy-skills.env`
   - Verify symbol format (swap vs spot)

## Debug tips
- Run prototype directly: `prototype/skill.py --help`
- Start with dry‑run or smallest size
