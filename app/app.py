from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Datum der Eröffnungsfeier: 6. Februar 2026, 20:00 Uhr (UTC+2)
    olympics_start = datetime(2026, 2, 6, 18, 0, 0)  # UTC
    return render_template("index.html", olympics_start=olympics_start)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
