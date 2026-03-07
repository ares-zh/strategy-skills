import matplotlib.pyplot as plt

def save_equity_curve(equity, out_path):
    plt.figure(figsize=(8,4))
    plt.plot(equity)
    plt.title("Equity Curve")
    plt.xlabel("Trades")
    plt.ylabel("Equity")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def save_html_report(spec, report, equity, out_path, img_path):
    html = f"""
    <html><head><title>Backtest Report</title></head><body>
    <h1>Backtest Report</h1>
    <h2>Strategy</h2>
    <pre>{spec}</pre>
    <h2>Metrics</h2>
    <ul>
      <li>Annualized: {report.annualized_return:.2%}</li>
      <li>Max Drawdown: {report.max_drawdown:.2%}</li>
      <li>Win Rate: {report.win_rate:.2%}</li>
      <li>Trades: {report.trades}</li>
    </ul>
    <h2>Equity Curve</h2>
    <img src="{img_path}" width="600" />
    </body></html>
    """
    with open(out_path, "w") as f:
        f.write(html)
