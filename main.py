from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    contact_data = {
        "name": name,
        "email": email,
        "message": message
    }

    with open("messages.txt", "a") as file:
        file.write(json.dumps(contact_data) + "\n")

    return jsonify({
        "success": True,
        "message": "Message received successfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)