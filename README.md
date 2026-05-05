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
