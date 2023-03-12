import os
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Привет от приложения Алексея"


@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

