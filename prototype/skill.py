import argparse
from strategies import parse_prompt
from backtest import run_backtest
from exchanges import BitgetAdapter, OrderRequest


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--exchange", default="bitget")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--order-type", default="market", choices=["market", "limit"])
    p.add_argument("--price", type=float, default=None)
    p.add_argument("--cost", type=float, default=None)
    args = p.parse_args()

    spec = parse_prompt(args.prompt)
    report = run_backtest(spec)

    print("=== Strategy Spec ===")
    print(spec)
    print("\n=== Backtest Report ===")
    print(report)

    if args.exchange == "bitget":
        adapter = BitgetAdapter(sandbox=True)
        order = OrderRequest(symbol="BTC/USDT", side="buy", qty=0.001, order_type=args.order_type, price=args.price)
        res = adapter.place_order(order, dry_run=args.dry_run, cost=args.cost)
        print("\n=== Execution (Bitget) ===")
        print(res)
    else:
        print("\nExchange not supported yet.")


if __name__ == "__main__":
    main()
