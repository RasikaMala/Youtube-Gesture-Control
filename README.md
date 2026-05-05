HEAD
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

Youtube-Gesture-Control
Real-time gesture-based YouTube control system using OpenCV, MediaPipe, and PyTorch, enabling touchless video interaction.
 YouTube Gesture Control System

 Overview
This project is a real-time gesture-based system that allows users to control YouTube videos using hand gestures. It eliminates the need for physical interaction like keyboard or mouse.

 Features
- Play / Pause control using gestures  
- Volume up / down  
- Forward / backward navigation  
- Fullscreen toggle  
- Subtitle on/off control  
- Real-time hand detection  

 Technologies Used
- Python  
- OpenCV  
- MediaPipe  
- PyTorch  
- Flask  
- PyAutoGUI  

 How It Works
1. Webcam captures real-time video using OpenCV  
2. MediaPipe detects 21 hand landmarks  
3. Landmarks are converted into feature values  
4. PyTorch model predicts the gesture  
5. PyAutoGUI performs corresponding actions  

 Project Structure
 project/
│── app.py
│── video_feed.py
│── utils.py
│── models/
│ ├── model.pth
│ ├── model_architecture.py
│── data/
│ ├── gestures.csv / excel file
│ ├── label.csv
│── static/
│── templates/

  How to Run
```bash
pip install -r requirements.txt
python app.py

Applications
Touchless interaction
Accessibility support
Smart systems

  Future Improvements
Add more gestures
Improve accuracy in low lighting
Mobile integration
 2a10a2e5c4f726c000a61478fc30d290568b84d4
