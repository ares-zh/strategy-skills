# Strategy Skills

**One‑line**: Turn a strategy prompt into backtest → deploy → auto‑execute, with exchange adapters (Bitget / Hyperliquid).

**Languages**: [English](README.md) | [中文](README.zh.md)

---

## 🚀 What is this?
Strategy Skills is a one‑stop pipeline that converts **strategy ideas** into **live execution**. You give a prompt (or file/image), we handle the rest: parse → backtest → optimize → deploy → monitor.

**Why it matters**: most strategy projects die between “idea” and “execution.” This closes that gap.

---

## ⚡ Quick Start

### Install as an OpenClaw Skill
```bash
openclaw skills install /Users/aresbot/.openclaw/workspace/skills/dist/strategy-skills.skill
```

### Configure (wizard)
```bash
/Users/aresbot/.openclaw/workspace/skills/strategy-skills/scripts/config_wizard.sh
```

### Use in OpenClaw
```
"Use Strategy Skills: EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
```

### File/Image input
- JSON strategy file: `--file examples/strategy.json`
- Screenshot OCR: `--image examples/strategy.png` (local OCR)

---

## 🧠 Architecture (Modules)
1) **Strategy Hub** – prompt/file/image → standardized DSL
2) **Backtest Engine** – metrics, equity curve, costs/slippage
3) **Execution Layer** – exchange adapters + risk controls
4) **Reporting** – receipts + PNG/HTML reports
5) **Console** – parameter tuning + live monitoring
6) **Skills API** – `load / backtest / deploy`

---

## ✅ What you get
- One‑click backtest
- Auto execution with risk guards
- Performance reports
- Standardized trade receipt (order → status → filled)
- Backtest PNG + HTML report
- Trade review PNG + HTML report
- Optional exchange‑referral flow

---

## 🎯 Use Cases
- “I have a strategy idea, but no infra.”
- “I want to test 5 strategies and deploy the best.”
- “I need an auto‑execution pipeline for Bitget/Hyperliquid.”

---

## 🧩 Roadmap
See `ROADMAP.md`.

## 📦 Build & Package
```bash
./scripts/build_skill.sh
```
This produces `dist/strategy-skills.skill`.

## 🧯 Risk & Safety
- See `RISK_GUARD.md`
- Logs & troubleshooting: `LOGGING.md`

## 🧪 Examples
- End‑to‑end demo: `examples/end_to_end.md`
- Strategy templates: `templates/`

## 📊 Visual Reports
- Backtest: `backtest_equity.png`, `backtest_report.html`
- Review: `trade_pnl.png`, `trade_review.html`

---

## 🛡️ Safety & Risk
- Auto‑execution requires explicit user confirmation
- Hard caps on position size & daily loss
- Hyperliquid size rounding to min step
- Full logs for audit

---

## 💸 Exchange Referral (Recommended)
- **Bitget (Recommended)**: Invite code **je5u0965** — https://partner.hdmune.cn/bg/paz1t8py (8折手续费返现)
- **Hyperliquid**: Invite code **JE5U0965** — https://app.hyperliquid.xyz/join/JE5U0965 (4% fee discount)

## 🤝 Contributing
See `CONTRIBUTING.md`.

---

## 📄 License
MIT
