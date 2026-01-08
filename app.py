from flask import Flask, render_template, request, jsonify
import os
import time

# Import your existing pipeline
from model import predict_from_file
from display import show_result, show_centered

app = Flask(__name__)

# Config
UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- ROUTES ----------

@app.route("/")
def index():
    """
    Home page (upload UI)
    """
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyze uploaded image using TFLite model
    and show result on OLED
    """
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save uploaded image
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        # Run inference using shared TFLite pipeline
        label, confidence = predict_from_file(filepath)
        confidence_pct = int(confidence * 100)

        # Update OLED
        show_result(label.upper(), confidence_pct)

        return jsonify({
            "status": "success",
            "diagnosis": label,
            "confidence": confidence_pct
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/health", methods=["GET"])
def health():
    """
    Health check endpoint
    """
    return jsonify({
        "status": "ok",
        "device": "raspberry-pi",
        "model": "tflite"
    })


# ---------- START SERVER ----------

if __name__ == "__main__":
    # Optional OLED message on web-app start
    show_centered("WEB MODE")
    time.sleep(1)
    show_centered("READY")

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=False
    )