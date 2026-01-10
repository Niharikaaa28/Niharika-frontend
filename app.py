from flask import Flask, render_template, request, jsonify
import os
import time
import threading
from display import show_web_mode
from power_switch import monitor_power_switch
# Import your existing pipeline
from model import predict_from_file
from buttons import detect_triple_click
from mode_switch import switch_to_device_mode
from display import show_result, show_centered
from flask import redirect



app = Flask(__name__)

import atexit
os.system("sudo /usr/local/bin/start_ap.sh")

def cleanup():
    os.system("sudo /usr/local/bin/stop_ap.sh")

atexit.register(cleanup)

# Config
UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global timer to track display reset
display_timer = None

def reset_display_to_ready():
    """Reset display to READY state after showing result"""
    time.sleep(5)  # Wait 5 seconds like main.py
    show_centered("READY")
    print("Display reset to READY")

# ---------- ROUTES ----------

@app.route("/")
def index():
    """
    Home page (upload UI)
    """
    return render_template("index.html")

@app.route("/generate_204")
def android_captive():
    return redirect("/")

# iOS captive check
@app.route("/hotspot-detect.html")
def ios_captive():
    return redirect("/")

@app.route("/captive.apple.com")
def apple_captive():
    return redirect("/")

# Windows captive check
@app.route("/ncsi.txt")
def windows_captive():
    return redirect("/")


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

        # Start timer to reset display to READY after 5 seconds
        global display_timer
        if display_timer and display_timer.is_alive():
            # Cancel previous timer if still running
            pass
        display_timer = threading.Thread(target=reset_display_to_ready, daemon=True)
        display_timer.start()

        return jsonify({
            "status": "success",
            "message": "Image analyzed successfully",
            "analysis": {
                "diagnosis": label,
                "confidence": confidence_pct
            }
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
        "status": "healthy",
        "message": "Server is running"
    })

@app.route("/switch-device", methods=["POST"])
def switch_device():
    threading.Thread(
        target=switch_to_device_mode,
        daemon=True
    ).start()

    return jsonify({"status": "switching"})

# ---------- START SERVER ----------

if __name__ == "__main__":
    # Optional OLED message on web-app start
    show_web_mode(duration=4)
    show_centered("READY")

    
    threading.Thread(
        target=monitor_power_switch,
        daemon=True
    ).start()


    app.run(
        host="0.0.0.0",
        port=80,
        debug=False
    )