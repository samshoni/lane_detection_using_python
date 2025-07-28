# 🛣️ Lane Detection Using Python & OpenCV

This project implements a simple lane detection system using computer vision techniques with Python and OpenCV. It processes video frames to identify road lane lines — an essential component of autonomous driving systems.

## ✅ Features
- Detects lane lines from road video footage
- Applies grayscale conversion, Gaussian blur, Canny edge detection
- Uses region of interest masking and Hough Transform for line detection
- Visualizes detected lane lines over original frames

## 📁 Project Structure

lane_detection_using_python/
├── videos/
│ └── test_video.mp4
├── lane_detector.py
└── README.md


## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies:

```bash
pip install opencv-python numpy
