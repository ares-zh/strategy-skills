# Strategy Skills

**One‑line**: Turn a strategy prompt into backtest → deploy → auto‑execute, with exchange adapters (Bitget / Hyperliquid).

**Languages**: [English](README.md) | [中文](README.zh.md)

---

## 🚀 What is this?
Strategy Skills is a one‑stop pipeline that converts **strategy ideas** into **live execution**. You give a prompt (or file/image), we handle the rest: parse → backtest → optimize → deploy → monitor.

**Why it matters**: most strategy projects die between “idea” and “execution.” This closes that gap.

---

## ⚡ Quick Start

### Install as an OpenClaw Skill (planned)
```bash
# placeholder: will provide install command once packaged
# openclaw skills install strategy-skills
```

### Use in OpenClaw
```
# Example
"Use Strategy Skills: EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
```

### File/Image input (planned)
- Upload strategy file (CSV/JSON/script)
- Or provide a screenshot/whiteboard → auto‑extraction

---

## 🧠 Architecture (Modules)
1) **Strategy Hub** – prompt/file/image → standardized DSL
2) **Backtest Engine** – metrics, equity curve, costs/slippage
3) **Execution Layer** – exchange adapters + risk controls
4) **Console** – parameter tuning + live monitoring
5) **Skills API** – `load / backtest / deploy`

---

## ✅ What you get
- One‑click backtest
- Auto execution with risk guards
- Performance reports
- Standardized trade receipt (order → status → filled)
- Optional exchange‑referral flow

---

## 🎯 Use Cases
- “I have a strategy idea, but no infra.”
- “I want to test 5 strategies and deploy the best.”
- “I need an auto‑execution pipeline for Bitget/Hyperliquid.”

---

## 🧩 Roadmap
See `ROADMAP.md`.

---

## 🛡️ Safety & Risk
- Auto‑execution requires explicit user confirmation
- Hard caps on position size & daily loss
- Full logs for audit

---

## 🤝 Contributing
See `CONTRIBUTING.md`.

---

## 📄 License
MIT
