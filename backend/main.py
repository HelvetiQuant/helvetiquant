
from flask import Flask, jsonify
from pybit.unified_trading import HTTP
import requests
from datetime import datetime
import os

app = Flask(__name__)

# Legge API Key e Secret da variabili d'ambiente (Railway)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

session = HTTP(testnet=False, api_key=API_KEY, api_secret=API_SECRET)

@app.route("/api/status")
def get_status():
    # Da sostituire con logica live del bot o segnali
    active_tokens = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    return jsonify({"active_tokens": active_tokens})

@app.route("/api/watchlist")
def get_watchlist():
    tickers = session.get_tickers(category="linear")["result"]["list"]
    sorted_tickers = sorted(tickers, key=lambda x: float(x["volume24h"]), reverse=True)
    top10 = [item["symbol"] for item in sorted_tickers[:10]]
    return jsonify({"watchlist": top10})

@app.route("/api/pnl/today")
def get_daily_pnl():
    # Statico per ora - da collegare con trading logger reale
    today_pnl = {"trades": 4, "total_pnl": 135}
    return jsonify(today_pnl)

@app.route("/api/sentiment")
def get_sentiment():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()
    today_data = data["data"][0]
    return jsonify({
        "value": today_data["value"],
        "label": today_data["value_classification"],
        "timestamp": datetime.utcfromtimestamp(int(today_data["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == "__main__":
    app.run(debug=True)
