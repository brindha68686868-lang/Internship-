import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")

    return jsonify({
        "status": "success",
        "message": "Production Ready Application"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Page not found"
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "error": "Internal server error"
    }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )