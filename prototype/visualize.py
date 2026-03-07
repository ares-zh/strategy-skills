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
    <html><head>
      <title>Backtest Report</title>
      <style>
        body {{ font-family: -apple-system, Arial; padding: 24px; background:#0b0f14; color:#e6edf3; }}
        .card {{ background:#111827; padding:16px; border-radius:12px; margin-bottom:16px; }}
        h1,h2 {{ margin:0 0 8px 0; }}
        .grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:12px; }}
        .metric {{ background:#0f172a; padding:12px; border-radius:10px; }}
        .metric span {{ color:#94a3b8; font-size:12px; }}
      </style>
    </head><body>
      <h1>Backtest Report</h1>
      <div class="card">
        <h2>Strategy</h2>
        <pre>{spec}</pre>
      </div>
      <div class="grid">
        <div class="metric"><span>Annualized</span><br>{report.annualized_return:.2%}</div>
        <div class="metric"><span>Max Drawdown</span><br>{report.max_drawdown:.2%}</div>
        <div class="metric"><span>Win Rate</span><br>{report.win_rate:.2%}</div>
        <div class="metric"><span>Trades</span><br>{report.trades}</div>
      </div>
      <div class="card">
        <h2>Equity Curve</h2>
        <img src="{img_path}" width="700" />
      </div>
    </body></html>
    """
    with open(out_path, "w") as f:
        f.write(html)
