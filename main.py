import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings("ignore")

import cv2 as cv
import torch
import pandas as pd
import mediapipe as mp
import pyautogui
import numpy as np
from collections import deque

from models.model_architecture import model
from utils import *

###################################################
# VARIABLES INITIALIZATION
###################################################

mode = 0
CSV_PATH = 'data/gestures.csv'

# Camera
WIDTH = 1028 // 2
HEIGHT = 720 // 2

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# Keypoints
TRAINING_KEYPOINTS = [i for i in range(0, 21, 4)]

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_drawing = mp.solutions.drawing_utils

# Load model
GESTURE_RECOGNIZER_PATH = 'models/model.pth'
model.load_state_dict(torch.load(GESTURE_RECOGNIZER_PATH, weights_only=True))

# Load labels
LABEL_PATH = 'data/label.csv'
labels = pd.read_csv(LABEL_PATH, header=None).values.flatten().tolist()

# ✅ Allowed gestures
ALLOWED_GESTURES = [
    'Play_Pause',
    'Vol_up_ytb',
    'Vol_down_ytb',
    'Vol_up_gen',
    'Vol_down_gen',
    'Forward',
    'Backward',
    'fullscreen',
    'Cap_Subt'
]

# Settings
CONF_THRESH = 0.9
GESTURE_HISTORY = deque([])
GEN_COUNTER = 0

###################################################
# MAIN LOOP
###################################################

while True:
    key = cv.waitKey(1)
    if key == ord('q'):
        break

    mode = select_mode(key, mode)
    class_id = get_class_id(key)

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    det_zone, _ = det_mouse_zones(frame)

    ###################################################
    # HAND DETECTION
    ###################################################

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            coordinates = calc_landmark_coordinates(frame_rgb, hand_landmarks)
            important_points = [coordinates[i] for i in TRAINING_KEYPOINTS]

            preprocessed = pre_process_landmark(important_points)

            d0 = calc_distance(coordinates[0], coordinates[5])
            pts = [coordinates[i] for i in [4, 8, 12]]
            distances = normalize_distances(d0, get_all_distances(pts))

            features = np.concatenate([preprocessed, distances])

            draw_info(frame, mode, class_id)
            logging_csv(class_id, mode, features, CSV_PATH)

            conf, pred = predict(features, model)

            gesture = labels[pred]

            # ✅ Filter unwanted gestures
            if gesture not in ALLOWED_GESTURES:
                gesture = "Unknown"

            ###################################################
            # CONTROL LOGIC
            ###################################################

            if (
                cv.pointPolygonTest(det_zone, coordinates[9], False) == 1
                and conf >= CONF_THRESH
            ):

                history = track_history(GESTURE_HISTORY, gesture)
                prev = history[-2] if len(history) >= 2 else history[0]

                if gesture in ALLOWED_GESTURES:

                    if gesture == 'Play_Pause' and prev != 'Play_Pause':
                        pyautogui.press('space')

                    elif gesture == 'Vol_up_ytb':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('up')

                    elif gesture == 'Vol_down_ytb':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('down')

                    elif gesture == 'Vol_up_gen':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('volumeup')

                    elif gesture == 'Vol_down_gen':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('volumedown')

                    elif gesture == 'Forward':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('right')

                    elif gesture == 'Backward':
                        GEN_COUNTER += 1
                        if GEN_COUNTER % 4 == 0:
                            pyautogui.press('left')

                    elif gesture == 'fullscreen' and prev != 'fullscreen':
                        pyautogui.press('f')

                    elif gesture == 'Cap_Subt' and prev != 'Cap_Subt':
                        pyautogui.press('c')

                    elif gesture == 'Neutral':
                        GEN_COUNTER = 0

            # Display gesture
            cv.putText(
                frame,
                f'{gesture} | {conf:.2f}',
                (int(WIDTH * 0.05), int(HEIGHT * 0.07)),
                cv.FONT_HERSHEY_COMPLEX,
                0.8,
                (0, 0, 255),
                1,
                cv.LINE_AA,
            )

    ###################################################
    # SHOW FRAME
    ###################################################
    cv.imshow('Gesture Control', frame)

###################################################
# CLEANUP
###################################################

cap.release()
cv.destroyAllWindows()