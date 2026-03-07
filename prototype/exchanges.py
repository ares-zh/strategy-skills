from dataclasses import dataclass

@dataclass
class OrderRequest:
    symbol: str
    side: str
    qty: float
    order_type: str = "market"
    price: float | None = None


class ExchangeAdapter:
    name = "base"

    def connect(self, credentials: dict):
        raise NotImplementedError

    def place_order(self, order: OrderRequest):
        raise NotImplementedError


class BitgetAdapter(ExchangeAdapter):
    name = "bitget"


class HyperliquidAdapter(ExchangeAdapter):
    name = "hyperliquid"
