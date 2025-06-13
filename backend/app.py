# backend/app.py

from flask import Flask, send_from_directory
import os

# Percorso assoluto alla cartella frontend
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend_live'))

app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')

# Homepage – serve index.html
@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# Serve altri file statici come script.js, style.css, ecc.
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)