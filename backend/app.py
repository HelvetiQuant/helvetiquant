from flask import Flask, render_template
app = Flask(__name__, template_folder='../frontend_live')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend_live'), 'index.html')

@app.route("/js")
def js():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend_live'), 'script.js')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port)