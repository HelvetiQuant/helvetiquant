
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Variabili globali per stato bot
bot_running = False

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "running" if bot_running else "stopped"
    })

@app.route("/start", methods=["POST"])
def start_bot():
    global bot_running
    bot_running = True
    return jsonify({"message": "Bot avviato"})

@app.route("/stop", methods=["POST"])
def stop_bot():
    global bot_running
    bot_running = False
    return jsonify({"message": "Bot fermato"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "Backend attivo"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

@app.route("/whale-alert", methods=["GET"])
def whale_alert():
    # Simulazione di dati (in produzione, chiamata reale con requests + API key)
    dummy_data = {
        "transactions": [
            {"timestamp": "2025-06-12 22:00", "symbol": "BTC", "amount_usd": 205000000, "from": "Unknown Wallet", "to": "Binance"},
            {"timestamp": "2025-06-12 21:57", "symbol": "ETH", "amount_usd": 46000000, "from": "Coinbase", "to": "Private Wallet"},
            {"timestamp": "2025-06-12 21:55", "symbol": "USDT", "amount_usd": 12500000, "from": "Unknown", "to": "Binance"},
        ]
    }
    return jsonify(dummy_data)

from whale import get_real_whale_alert

@app.route("/whale-alert", methods=["GET"])
def whale_alert():
    data = get_real_whale_alert()
    return jsonify(data)
