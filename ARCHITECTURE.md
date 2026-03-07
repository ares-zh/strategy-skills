# Strategy Skills — Technical Architecture

## 1) High‑Level Flow
```
User Prompt / File / Image
        ↓
Strategy Hub (Parser + DSL)
        ↓
Backtest Engine (data + metrics)
        ↓
Risk Engine (limits + guards)
        ↓
Execution Layer (Exchange Adapters)
        ↓
Reporting (PnL + metrics)
```

## 2) Modules

### 2.1 Strategy Hub
- **Inputs**: prompt / file / image
- **Output**: StrategySpec (DSL)
- **Responsibilities**:
  - parse & validate
  - normalize symbol/timeframe
  - generate rules

### 2.2 Backtest Engine
- **Data Sources**: kline/funding/oi
- **Outputs**: equity curve, metrics
- **Metrics**: annualized return, max drawdown, win rate

### 2.3 Risk Engine
- Position limits
- Daily loss limit
- Cooldown after loss
- Hard stop‑loss

### 2.4 Execution Layer
- Exchange adapter interface
- Bitget adapter
- Hyperliquid adapter
- Order normalization

### 2.5 Reporting
- Daily/weekly reports
- PnL + drawdown
- Trade log

## 3) Data Contracts

### StrategySpec
```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1h",
  "direction": "long",
  "entry": "EMA20/50 cross",
  "exit": "reverse cross",
  "sl": 0.02,
  "tp": 0.04
}
```

### OrderRequest
```json
{
  "symbol": "BTC-PERP",
  "side": "buy",
  "qty": 0.01,
  "type": "market",
  "price": null
}
```

## 4) Adapter Interface
```ts
interface IExchangeAdapter {
  name: string
  connect(credentials): Promise<void>
  getBalance(): Promise<Balance>
  getPositions(): Promise<Position[]>
  placeOrder(order: OrderRequest): Promise<OrderResult>
  cancelOrder(orderId: string): Promise<void>
  getMarketData(symbol, timeframe): Promise<Candle[]>
}
```

## 5) Deployment
- Local CLI → first prototype
- OpenClaw Skill packaging → end user interface

## 6) Security
- API keys stored encrypted
- No auto‑execute without explicit consent
- Full audit logs
