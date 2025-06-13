from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "HelvetiQuant è attivo"

@app.route("/dashboard")
def dashboard():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend_live'), 'index.html')

@app.route("/js")
def js():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend_live'), 'script.js')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port)