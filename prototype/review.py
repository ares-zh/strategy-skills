import csv
import matplotlib.pyplot as plt


def load_trades(csv_path: str):
    trades = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trades.append(row)
    return trades


def save_trade_pnl_chart(trades, out_path):
    pnl = [float(t["pnl"]) for t in trades]
    eq = []
    s = 0
    for p in pnl:
        s += p
        eq.append(s)

    plt.figure(figsize=(8,4))
    plt.plot(eq)
    plt.title("Trade PnL Curve")
    plt.xlabel("Trades")
    plt.ylabel("PnL")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def save_review_html(trades, out_path, img_path):
    total = sum(float(t["pnl"]) for t in trades)
    html = f"""
    <html><head>
      <title>Trade Review</title>
      <style>
        body {{ font-family: -apple-system, Arial; padding: 24px; background:#0b0f14; color:#e6edf3; }}
        .card {{ background:#111827; padding:16px; border-radius:12px; margin-bottom:16px; }}
        table {{ width:100%; border-collapse: collapse; }}
        th,td {{ border-bottom:1px solid #1f2937; padding:8px; text-align:left; }}
      </style>
    </head><body>
      <h1>Trade Review</h1>
      <div class="card">
        <h2>Summary</h2>
        <div>Total PnL: {total:.2f}</div>
        <div>Trades: {len(trades)}</div>
      </div>
      <div class="card">
        <h2>Chart</h2>
        <img src="{img_path}" width="700" />
      </div>
      <div class="card">
        <h2>Trades</h2>
        <table>
          <tr><th>time</th><th>symbol</th><th>side</th><th>qty</th><th>price</th><th>pnl</th></tr>
          {''.join([f"<tr><td>{t['time']}</td><td>{t['symbol']}</td><td>{t['side']}</td><td>{t['qty']}</td><td>{t['price']}</td><td>{t['pnl']}</td></tr>" for t in trades])}
        </table>
      </div>
    </body></html>
    """
    with open(out_path, "w") as f:
        f.write(html)
