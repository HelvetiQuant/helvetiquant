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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)