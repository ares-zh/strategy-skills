import argparse
from strategies import parse_prompt
from backtest import run_backtest
from exchanges import BitgetAdapter, OrderRequest


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=False)
    p.add_argument("--file", required=False)
    p.add_argument("--image", required=False)
    p.add_argument("--exchange", default="bitget")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--order-type", default="market", choices=["market", "limit"])
    p.add_argument("--price", type=float, default=None)
    p.add_argument("--cost", type=float, default=None)
    p.add_argument("--skip-backtest", action="store_true")
    args = p.parse_args()

    if args.file:
        from strategies import parse_file
        spec = parse_file(args.file)
    elif args.image:
        from strategies import parse_image
        spec = parse_image(args.image)
    else:
        if not args.prompt:
            raise ValueError("Provide --prompt or --file or --image")
        spec = parse_prompt(args.prompt)
    print("=== Strategy Spec ===")
    print(spec)

    if not args.skip_backtest:
        report, equity = run_backtest(spec)
        print("\n=== Backtest Report ===")
        print(report)
        try:
            from visualize import save_equity_curve, save_html_report
            save_equity_curve(equity, "backtest_equity.png")
            save_html_report(spec, report, equity, "backtest_report.html", "backtest_equity.png")
            print("\nSaved: backtest_equity.png, backtest_report.html")
        except Exception as e:
            print("Visualization skipped:", e)
    else:
        print("\n=== Backtest Report ===")
        print("Skipped")

    if args.exchange == "bitget":
        adapter = BitgetAdapter(sandbox=True)
        # spot order (simplest)
        order = OrderRequest(symbol="BTC/USDT", side="buy", qty=0.001, order_type=args.order_type, price=args.price)
        res = adapter.place_order(order, dry_run=args.dry_run, cost=args.cost)
        print("\n=== Execution (Bitget) ===")
        print(res)

        # if live order, fetch status
        if not args.dry_run and res and isinstance(res, dict) and res.get("id"):
            status = adapter.get_order(res["id"], order.symbol)
            print("\n=== Order Status ===")
            print(status)
    elif args.exchange == "hyperliquid":
        from exchanges import HyperliquidAdapter
        adapter = HyperliquidAdapter(sandbox=True)
        order = OrderRequest(symbol="BTC", side="buy", qty=0.00022, order_type=args.order_type, price=args.price)
        res = adapter.place_order(order, dry_run=args.dry_run)
        print("\n=== Execution (Hyperliquid) ===")
        print(res)
    else:
        print("\nExchange not supported yet.")


if __name__ == "__main__":
    main()
