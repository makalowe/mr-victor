"""
MR VICTOR / ElecConform — Application Flask
Site vitrine pour electricien (mise en conformite RGIE Wallonie & Bruxelles)
"""

import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "elecconform-dev-key")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/merci")
def merci():
    return render_template("merci.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
