
import os
import time
import threading
from datetime import datetime
from flask import Flask, jsonify
from trade_simulator import TradeSimulator
from report_generator import generate_daily_report
from telegram_notifier import send_telegram_message
from bybit_data_fetcher import get_ticker
import requests

# Inizializza Flask app
app = Flask(__name__)

# Inizializza simulatore
simulator = TradeSimulator(starting_balance=3600)

# ROUTES VISIBILI SULLA DASHBOARD PUBBLICA
@app.route("/")
def home():
    return "✅ HelvetiQuant è attivo e funzionante"

@app.route("/status")
def status():
    return jsonify({
        "status": "online",
        "balance": simulator.get_balance(),
        "open_trades": simulator.get_open_trades(),
        "time": datetime.now().isoformat()
    })

@app.route("/api/status")
def api_status():
    try:
        ticker = get_ticker("1000PEPEUSDT")
        return jsonify({
            "symbol": "1000PEPEUSDT",
            "price": ticker["price"],
            "funding_rate": ticker["funding_rate"],
            "volume_24h": ticker["volume_24h"],
            "gpt": "LONG 1000PEPEUSDT @ 25x per eccesso dump",
            "claude": "Confermato LONG (RSI basso + funding positivo)",
            "signal": "PUMP",
            "watchlist": ["PEPE", "SHIB", "BONK"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# FUNZIONI OPERATIVE
def daily_report_and_notify():
    trades = simulator.get_trade_history()
    balance = simulator.get_balance()
    pdf_path = generate_daily_report(balance=balance, trades=trades)
    send_telegram_message(f"📄 Report giornaliero generato. Bilancio: {balance:.2f} USDT")
    with open(pdf_path, "rb") as f:
        requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendDocument",
            data={"chat_id": os.getenv("TELEGRAM_CHAT_ID")},
            files={"document": f}
        )

def trading_loop():
    while True:
        now = datetime.utcnow()
        if now.hour == 18 and now.minute == 0:  # 20:00 CET = 18:00 UTC
            print("🕗 Generazione report giornaliero")
            daily_report_and_notify()
            time.sleep(60)
        else:
            time.sleep(30)

# MAIN
if __name__ == "__main__":
    # Avvia loop trading in thread separato
    t = threading.Thread(target=trading_loop)
    t.daemon = True
    t.start()

    # Avvia server Flask su Railway
    app.run(host="0.0.0.0", port=8080)
