# Hyperliquid Strategy Skills — 项目说明

## 目标
打造可插拔“策略→回测→可视化→自动执行”的 OpenClaw Skill，先跑通 Hyperliquid，再扩展至其它交易所。

## 核心模块
1) Strategy Hub：策略导入/标准化 DSL
2) Backtest Engine：回测与指标输出
3) Execution Layer：Hyperliquid 下单与风控
4) Console：参数配置 + 回测 + 实盘状态
5) Skills API：load/backtest/deploy

## 商业模式（隐性）
- 返佣/带量合作：邀请码、成交量阶梯返佣
- 策略展示位：平台内曝光

## 里程碑（4 周）
- W1：策略 DSL + 回测雏形
- W2：Hyperliquid 执行层
- W3：可视化控制台
- W4：OpenClaw Skills 接口

## 产出文件
- `reports/hyperliquid_skill_mvp_roadmap.md`
- `reports/hyperliquid_partner_pitch.md`
- `reports/hyperliquid_partner_pitch_business.md`
