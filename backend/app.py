from flask import Flask, jsonify, send_from_directory
import random, time, os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('frontend_live', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('frontend_live', 'script.js')

@app.route('/price')
def price():
    return jsonify({
        "token": "XRPUSDT",
        "price": round(random.uniform(0.45, 0.48), 5),
        "timestamp": int(time.time())
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)