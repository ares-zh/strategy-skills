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

    plt.style.use('dark_background')
    plt.figure(figsize=(8,4))
    color = "#22c55e" if eq[-1] >= 0 else "#ef4444"
    plt.plot(eq, color=color)
    plt.title("Trade PnL Curve")
    plt.xlabel("Trades")
    plt.ylabel("PnL")
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def save_pnl_histogram(trades, out_path):
    pnl = [float(t["pnl"]) for t in trades]
    plt.style.use('dark_background')
    plt.figure(figsize=(6,4))
    plt.hist(pnl, bins=10, color="#60a5fa")
    plt.title("PnL Distribution")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def compute_stats(trades):
    pnl = [float(t["pnl"]) for t in trades]
    wins = [p for p in pnl if p > 0]
    losses = [p for p in pnl if p < 0]
    win_rate = len(wins) / len(pnl) if pnl else 0
    profit_factor = (sum(wins) / abs(sum(losses))) if losses else float('inf')
    return {
        "total_pnl": sum(pnl),
        "trades": len(pnl),
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "avg_win": sum(wins)/len(wins) if wins else 0,
        "avg_loss": sum(losses)/len(losses) if losses else 0,
    }


def save_review_html(trades, out_path, img_path, hist_path):
    stats = compute_stats(trades)
    html = f"""
    <html><head>
      <title>Trade Review</title>
      <style>
        body {{ font-family: -apple-system, Arial; padding: 24px; background:#0b0f14; color:#e6edf3; }}
        .card {{ background:#111827; padding:16px; border-radius:12px; margin-bottom:16px; }}
        table {{ width:100%; border-collapse: collapse; }}
        th,td {{ border-bottom:1px solid #1f2937; padding:8px; text-align:left; }}
        .grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:12px; }}
        .metric {{ background:#0f172a; padding:12px; border-radius:10px; }}
        .metric span {{ color:#94a3b8; font-size:12px; }}
      </style>
    </head><body>
      <h1>Trade Review (MT4-style)</h1>
      <div class="grid">
        <div class="metric"><span>Total PnL</span><br>{stats['total_pnl']:.2f}</div>
        <div class="metric"><span>Trades</span><br>{stats['trades']}</div>
        <div class="metric"><span>Win Rate</span><br>{stats['win_rate']:.2%}</div>
        <div class="metric"><span>Profit Factor</span><br>{stats['profit_factor']:.2f}</div>
      </div>
      <div class="grid">
        <div class="metric"><span>Avg Win</span><br>{stats['avg_win']:.2f}</div>
        <div class="metric"><span>Avg Loss</span><br>{stats['avg_loss']:.2f}</div>
      </div>
      <div class="card">
        <h2>Equity / PnL Curve</h2>
        <img src="{img_path}" width="700" />
      </div>
      <div class="card">
        <h2>PnL Distribution</h2>
        <img src="{hist_path}" width="500" />
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
