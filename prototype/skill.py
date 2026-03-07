import argparse
from strategies import parse_prompt
from backtest import run_backtest


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    args = p.parse_args()

    spec = parse_prompt(args.prompt)
    report = run_backtest(spec)

    print("=== Strategy Spec ===")
    print(spec)
    print("\n=== Backtest Report ===")
    print(report)
    print("\nNext: deploy to exchange (stub).")


if __name__ == "__main__":
    main()
