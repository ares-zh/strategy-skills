# Hyperliquid Trade Receipt Format

Example:
```
{
  "status": "ok",
  "response": {
    "type": "order",
    "data": {
      "statuses": [
        {
          "filled": {
            "totalSz": "0.00022",
            "avgPx": "67780.0",
            "oid": 341367125495
          }
        }
      ]
    }
  }
}
```

Flow: place order → read `filled` fields → normalize into standard receipt.
