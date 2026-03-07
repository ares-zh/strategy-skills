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
        self.exchange = None
        self.wallet = None

    def connect(self, credentials: dict | None = None):
        from hyperliquid.exchange import Exchange
        from hyperliquid.utils import constants
        from eth_account import Account

        pk = os.getenv("HYPERLIQUID_PRIVATE_KEY")
        wallet_addr = os.getenv("HYPERLIQUID_WALLET")
        if not pk or not wallet_addr:
            raise ValueError("Missing Hyperliquid env vars")

        api_url = constants.TESTNET_API_URL if self.sandbox else constants.MAINNET_API_URL
        wallet = Account.from_key(pk)
        self.wallet = wallet_addr
        self.exchange = Exchange(wallet, api_url, account_address=wallet_addr)

    def place_order(self, order: OrderRequest, dry_run: bool = True, cost: float | None = None):
        if dry_run:
            return {"status": "dry-run", "order": order, "cost": cost}
        if not self.exchange:
            self.connect(None)

        is_buy = order.side.lower() == "buy"
        if order.order_type == "limit":
            return self.exchange.order(order.symbol, is_buy, order.qty, order.price, {"limit": {"tif": "Gtc"}})
        else:
            return self.exchange.order(order.symbol, is_buy, order.qty, order.price or 0, {"market": {}})

    def get_order(self, order_id: str, symbol: str):
        # Hyperliquid SDK has openOrders / userState; order status retrieval TBD
        return {"status": "pending", "order_id": order_id, "symbol": symbol}
