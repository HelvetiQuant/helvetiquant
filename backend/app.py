from flask import Flask, jsonify, request, send_from_directory
import os
from whale import get_real_whale_alert

app = Flask(__name__, static_folder='../frontend_live', static_url_path='')

bot_running = False

@app.route("/")
def serve_dashboard():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running" if bot_running else "stopped"})

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

@app.route("/whale-alert", methods=["GET"])
def whale_alert():
    data = get_real_whale_alert()
    return jsonify(data)

@app.route("/<path:path>")
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
