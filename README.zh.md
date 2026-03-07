# Strategy Skills（中文）

**一句话**：把策略 prompt 变成回测 → 部署 → 自动执行，并支持 Bitget / Hyperliquid 适配器。

## 为什么做这个
传统策略交易割裂且成本高。Strategy Skills 让 **prompt → 回测 → 执行** 变成一键流程。

## 功能（MVP）
- 策略 prompt 解析（后续支持文件/图片）
- 回测占位版（指标 + 报告）
- 交易所适配器骨架（Bitget/Hyperliquid）
- 风控（规划中）

## 快速开始
```bash
cd prototype
python3 skill.py --prompt "EMA20/50 cross on BTCUSDT, 1h, long only, SL 2%, TP 4%"
```

## 文档
- PRD：`PRD.md`
- 项目概览：`PROJECT_OVERVIEW.md`

## 路线图
见 `ROADMAP.md`

## 贡献
见 `CONTRIBUTING.md`

## 许可证
MIT
