# Strategy Skills（中文）

**一句话**：把策略 prompt 变成回测 → 部署 → 自动执行，并支持 Bitget / Hyperliquid 适配器。

**语言**： [English](README.md) | [中文](README.zh.md)

---

## 🚀 这是什么？
Strategy Skills 是一条龙策略执行管线：**策略想法 → 自动回测 → 一键部署 → 实盘执行**。

痛点：大多数策略死在“想法”和“执行”之间。我们把这条链路打通。

---

## ⚡ 快速开始

### 作为 OpenClaw Skill 安装（规划中）
```bash
# 占位：打包后提供安装命令
# openclaw skills install strategy-skills
```

### 在 OpenClaw 中使用
```
示例：
“使用 Strategy Skills：EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%”
```

### 文件/图片输入（规划中）
- 上传策略文件（CSV/JSON/脚本片段）
- 或提供截图/白板 → 自动还原策略

---

## 🧠 模块架构
1) **Strategy Hub**：prompt/文件/图片 → 标准化 DSL
2) **Backtest Engine**：回测指标、净值曲线、滑点模型
3) **Execution Layer**：交易所适配 + 风控
4) **Console**：参数调优 + 实盘监控
5) **Skills API**：`load / backtest / deploy`

---

## ✅ 你会得到什么
- 一键回测
- 自动执行 + 风控
- 绩效报表
- 标准化成交回执（下单→状态→成交）
- 交易所返佣入口（可选）

---

## 🎯 适用场景
- “我有策略想法，但没有系统”
- “我想快速筛 5 个策略再部署”
- “我要 Bitget/Hyperliquid 自动执行管线”

---

## 🧩 路线图
见 `ROADMAP.md`。

---

## 🛡️ 安全与风控
- 自动执行必须用户确认
- 仓位与日亏损硬限制
- Hyperliquid 最小步进自动取整
- 完整操作日志

---

## 🤝 贡献
见 `CONTRIBUTING.md`。

---

## 📄 许可证
MIT
