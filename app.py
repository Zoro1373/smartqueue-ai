from flask import Flask, jsonify, render_template
import json
import statistics
from pathlib import Path

app = Flask(__name__)

METADATA_PATH = Path(__file__).parent / "data" / "metadata_nms_test.json"

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/status")
def status():
    return jsonify({
        "project": "SmartQueue AI",
        "backend": "online",
        "metadata_available": METADATA_PATH.is_file()
    })

@app.route("/api/summary")
def summary():
    if not METADATA_PATH.is_file():
        return jsonify({"error": "Metadata file not found"}), 404

    with METADATA_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    frames = data.get("frames", [])
    counts = [len(frame.get("objects", [])) for frame in frames]
    confidences = [
        obj.get("confidence", 0)
        for frame in frames
        for obj in frame.get("objects", [])
    ]

    scopes = sorted({
        frame.get("fields", {}).get("roi_scope", "unknown")
        for frame in frames
    })

    return jsonify({
        "project": data.get("pipeline", "SmartQueue AI"),
        "source": data.get("source", ""),
        "frames_processed": len(frames),
        "total_detections": sum(counts),
        "average_detections": round(statistics.mean(counts), 2) if counts else 0,
        "min_detections": min(counts, default=0),
        "max_detections": max(counts, default=0),
        "average_confidence": round(statistics.mean(confidences), 3) if confidences else 0,
        "min_confidence": data.get("min_confidence"),
        "roi_scope": scopes,
        "timeline": [
            {
                "frame": frame.get("frame", i),
                "detections": len(frame.get("objects", [])),
                "occupancy": frame.get("fields", {}).get("roi_occupancy_count", 0)
            }
            for i, frame in enumerate(frames)
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
