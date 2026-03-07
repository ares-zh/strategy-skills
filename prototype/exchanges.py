from dataclasses import dataclass
import os
import ccxt

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

    def place_order(self, order: OrderRequest, dry_run: bool = True):
        raise NotImplementedError

    def get_order(self, order_id: str, symbol: str):
        raise NotImplementedError


class BitgetAdapter(ExchangeAdapter):
    name = "bitget"

    def __init__(self, sandbox: bool = True):
        self.sandbox = sandbox
        self.client = None

    def connect(self, credentials: dict | None = None):
        key = os.getenv("BITGET_API_KEY")
        secret = os.getenv("BITGET_API_SECRET")
        passphrase = os.getenv("BITGET_API_PASSPHRASE")
        if not key or not secret or not passphrase:
            raise ValueError("Missing Bitget API env vars")

        self.client = ccxt.bitget({
            "apiKey": key,
            "secret": secret,
            "password": passphrase,
            "enableRateLimit": True,
            "options": {"defaultType": "swap", "createMarketBuyOrderRequiresPrice": False},
        })
        # enable sandbox if supported
        try:
            self.client.set_sandbox_mode(self.sandbox)
        except Exception:
            pass

    def place_order(self, order: OrderRequest, dry_run: bool = True, cost: float | None = None):
        if dry_run:
            return {"status": "dry-run", "order": order, "cost": cost}
        if not self.client:
            self.connect(None)
        params = {}
        if cost is not None:
            params["cost"] = cost
        return self.client.create_order(
            symbol=order.symbol,
            type=order.order_type,
            side=order.side,
            amount=order.qty,
            price=order.price,
            params=params,
        )

    def get_order(self, order_id: str, symbol: str):
        if not self.client:
            self.connect(None)
        return self.client.fetch_order(order_id, symbol)


class HyperliquidAdapter(ExchangeAdapter):
    name = "hyperliquid"

    def __init__(self, sandbox: bool = True):
        self.sandbox = sandbox
        self.client = None

    def connect(self, credentials: dict | None = None):
        # TODO: wire Hyperliquid SDK / REST
        # env vars: HYPERLIQUID_PRIVATE_KEY, HYPERLIQUID_WALLET
        raise NotImplementedError("Hyperliquid adapter not wired yet")

    def place_order(self, order: OrderRequest, dry_run: bool = True, cost: float | None = None):
        if dry_run:
            return {"status": "dry-run", "order": order, "cost": cost}
        raise NotImplementedError("Hyperliquid adapter not wired yet")

    def get_order(self, order_id: str, symbol: str):
        raise NotImplementedError("Hyperliquid adapter not wired yet")
