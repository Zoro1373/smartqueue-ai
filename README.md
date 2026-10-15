# SmartQueue AI Dashboard

Intelligent checkout queue monitoring dashboard built with Flask and computer vision video analytics metadata.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)

---

## 📌 Overview

**SmartQueue AI** is a lightweight web dashboard for visualizing and analyzing computer vision person-detection metadata (e.g. from PipeGen / TensorRT pipelines). It processes detection metrics across frames to provide immediate operational insights into checkout occupancy, average detections, and confidence metrics.

---

## 🚀 Features

- **Real-Time Analytics Summary**: Instant KPIs including total frames processed, total detections, average detections per frame, and average model confidence.
- **Interactive Visual Trend**: Canvas-based frame-by-frame line chart showing detection trends across the processed video.
- **RESTful Endpoints**:
  - `GET /api/status`: Health check and metadata file availability.
  - `GET /api/summary`: Aggregated metrics, confidence scores, ROI scope, and per-frame timeline data.
- **Dark Mode UI**: Sleek, responsive, and minimalist dashboard designed for monitor stations and desktop views.

---

## 📂 Project Structure

```
smartqueue-ai/
├── app.py                      # Flask backend and API endpoints
├── requirements.txt            # Python dependencies (Flask)
├── data/
│   └── metadata_nms_test.json  # Precomputed CV detection metadata
├── templates/
│   └── index.html              # Modern dark-mode dashboard UI & chart
└── README.md                   # Project documentation
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Zoro1373/smartqueue-ai.git
cd smartqueue-ai
```

### 2. Set Up Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**On Linux / macOS / WSL:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch the Dashboard

```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📊 Data Source

The dashboard reads `data/metadata_nms_test.json`, which contains bounding box, confidence scores, and ROI metadata generated from a pre-processed video pipeline.

### Limitations & Next Steps
- **ROI Scope**: Currently covers the full frame (`whole_frame_default`). Future iterations will support custom polygonal checkout zones.
- **Tracking IDs**: Person tracking IDs are not yet enabled; counts represent detections per frame rather than unique individuals across time.
- **Queue Length Verification**: Current detection counts reflect raw detected persons and serve as preliminary analytics.

---

## 📄 License

MIT License. Feel free to use and adapt for hackathons and production prototypes.
