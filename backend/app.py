# backend/app.py

from flask import Flask, send_from_directory
import os

# Percorso assoluto verso frontend_live
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend_live'))

app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)