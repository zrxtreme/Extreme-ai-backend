from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Extreme AI Backend is running."

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "")
    return jsonify({"status": "success", "message": f"Image generated from prompt: {prompt} (demo)"})

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.json
    prompt = data.get("prompt", "")
    return jsonify({"status": "success", "message": f"Video generated from prompt: {prompt} (demo)"})

@app.route("/voice-to-text", methods=["POST"])
def voice_to_text():
    return jsonify({"status": "success", "text": "Transcribed voice (demo)"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    return jsonify({"response": f"You said: {message} (demo AI reply)"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
