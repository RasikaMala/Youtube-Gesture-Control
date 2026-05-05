# Controlling YouTube Using Hand Gestures

## Project Overview
This project allows users to control YouTube playback using hand gestures detected through a webcam. It leverages computer vision libraries to detect hand positions and perform actions such as play, pause, volume control, and skipping videos.

The goal is to provide a **touchless, interactive experience** for controlling video playback, enhancing accessibility and convenience.

---

## Features
- Play and pause YouTube videos using specific hand gestures.
- Adjust volume with hand movements.
- Skip forward or backward in a video with gestures.
- Real-time gesture recognition using webcam input.
- Easy to use and does not require external hardware beyond a standard webcam.

---

## Technologies Used
- **Python 3.x**
- **OpenCV** – for video capture and image processing.
- **MediaPipe** – for hand landmark detection.
- **PyAutoGUI** – to control YouTube through keyboard shortcuts.
- **Dlib** – optional for hand shape detection enhancement.
- **Web Browser** – YouTube playback control via keyboard shortcuts.

---

## Installation

1. **Clone the repository**
```bash
git clone //https://github.com/vinay4169e/gesture-youtube-control.git
cd gesture-youtube-control


Install dependencies

pip install opencv-python mediapipe pyautogui dlib


Run the project

python main.py