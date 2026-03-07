# Standard Trade Receipt Format

Example fields returned after order placement:

```
{
  "id": "1414174677018832896",
  "symbol": "BTC/USDT",
  "type": "market",
  "side": "buy",
  "price": 67934.82,
  "amount": 0.000294,
  "cost": 19.9728,
  "status": "closed",
  "fee": {"cost": 2.058e-07, "currency": "BTC"}
}
```

Flow: place order → fetch order status → return standardized receipt.
