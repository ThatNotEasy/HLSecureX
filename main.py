import os
from flask import Flask, send_file, jsonify, abort
from flask_cors import CORS
from modules.hls_secure import HLSecureX

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

hls = HLSecureX()


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the local HLS server!"})

@app.route("/key/<key_id>", methods=["GET"])
def serve_key(key_id):
    if key_id != hls.key_id:  # Validate key_id dynamically
        abort(403, description="Unauthorized access to key")
    return send_file(hls.content_key_file, as_attachment=True)

@app.route("/playlist/<filename>", methods=["GET"])
def serve_playlist(filename):
    playlist_path = os.path.join(hls.hls_dir, filename)
    if os.path.exists(playlist_path):
        return send_file(playlist_path, mimetype="application/vnd.apple.mpegurl")
    else:
        abort(404, description="Playlist file not found")

@app.route("/segment/<filename>", methods=["GET"])
def serve_segment(filename):
    segment_path = os.path.join(hls.hls_dir, filename)
    if os.path.exists(segment_path):
        return send_file(segment_path, mimetype="video/iso.segment")
    else:
        abort(404, description="Segment file not found")

if __name__ == "__main__":
    try:
        hls.setup_workflow(key_uri="http://localhost:5000/key")
        print("HLS generation complete!")

        print("Starting Flask server...")
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        print(f"Error during HLS generation or server startup: {e}")