from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/price")
def price():
    return jsonify({
        "token": "XRPUSDT",
        "price": round(random.uniform(0.45, 0.48), 5),
        "timestamp": int(time.time())
    })

@app.route("/signal")
def signal():
    return jsonify({
        "action": random.choice(["BUY", "HOLD", "SELL"]),
        "confidence": round(random.uniform(0.6, 0.95), 2)
    })

@app.route("/trades")
def trades():
    return jsonify([
        {"entry": 0.45678, "exit": 0.47890, "profit": "+4.83%"},
        {"entry": 0.46321, "exit": 0.44500, "profit": "-3.94%"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)