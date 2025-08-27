from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/health")
def health():
    # Randomly simulate failure
    if random.randint(1, 10) > 8:
        return jsonify({"status": "unhealthy"}), 500
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
