import cv2
import mediapipe as mp
import numpy as np

class PhantomEngine():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode = False,
            max_num_hands=1,
            min_detection_confidence=0.7, 
            min_tracking_confidence=0.5,
        )

    
    def run():
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened():
            success, image = cap.read()
            if not success: continue

            image = cv2.flip(image, 1)
            RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(RGB_image)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    thumb = hand_landmarks.landmark[4]
                    index = hand_landmarks.landmark[8]


            if cv2.waitKey(5) & 0xFF == 27:
                break 

        cap.release()
