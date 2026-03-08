# Strategy Skills（中文）

**一句话**：把策略 prompt 变成回测 → 部署 → 自动执行，并支持 Bitget / Hyperliquid 适配器。

**语言**： [English](README.md) | [中文](README.zh.md)

---

## 🚀 这是什么？
Strategy Skills 是一条龙策略执行管线：**策略想法 → 自动回测 → 一键部署 → 实盘执行**。

痛点：大多数策略死在“想法”和“执行”之间。我们把这条链路打通。

---

## ⚡ 快速开始

### 作为 OpenClaw Skill 安装
```bash
openclaw skills install /Users/aresbot/.openclaw/workspace/skills/dist/strategy-skills.skill
```

### 配置向导
```bash
/Users/aresbot/.openclaw/workspace/skills/strategy-skills/scripts/config_wizard.sh
```

### 在 OpenClaw 中使用
```
示例：
“使用 Strategy Skills：EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%”
```

### 文件/图片输入
- JSON 策略文件：`--file examples/strategy.json`
- 截图 OCR：`--image examples/strategy.png`（本地 OCR）

---

## 🧠 模块架构
1) **Strategy Hub**：prompt/文件/图片 → 标准化 DSL
2) **Backtest Engine**：回测指标、净值曲线、滑点模型
3) **Execution Layer**：交易所适配 + 风控
4) **Reporting**：回执 + PNG/HTML 报告
5) **Console**：参数调优 + 实盘监控
6) **Skills API**：`load / backtest / deploy`

---

## ✅ 你会得到什么
- 一键回测
- 自动执行 + 风控
- 绩效报表
- 标准化成交回执（下单→状态→成交）
- 回测 PNG + HTML 报告
- 交易复盘 PNG + HTML 报告
- 交易所返佣入口（可选）

---

## 🎯 适用场景
- “我有策略想法，但没有系统”
- “我想快速筛 5 个策略再部署”
- “我要 Bitget/Hyperliquid 自动执行管线”

---

## 🧩 路线图
见 `ROADMAP.md`。

## 📦 打包发布
```bash
./scripts/build_skill.sh
```
生成 `dist/strategy-skills.skill`。

## 🧯 风控与安全
- 见 `RISK_GUARD.md`
- 日志与排错：`LOGGING.md`

## 🧪 示例
- 端到端 Demo：`examples/end_to_end.md`
- 策略模板：`templates/`

## 📊 可视化产物
- 回测：`backtest_equity.png`, `backtest_report.html`
- 复盘：`trade_pnl.png`, `trade_review.html`

---

## 🛡️ 安全与风控
- 自动执行必须用户确认
- 仓位与日亏损硬限制
- Hyperliquid 最小步进自动取整
- 完整操作日志

---

## 💸 交易所返佣入口（建议）
- **Bitget**：邀请码 **je5u0965** — https://partner.hdmune.cn/bg/paz1t8py（手续费 8 折返现）
- **Hyperliquid**：邀请码 **JE5U0965** — https://app.hyperliquid.xyz/join/JE5U0965（4% 折扣）

## 🤝 贡献
见 `CONTRIBUTING.md`。

---

## 📄 许可证
MIT
