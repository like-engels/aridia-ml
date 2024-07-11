import os
import pickle
import mediapipe as mediapipe
import cv2

mp_hands = mediapipe.solutions.hands
mp_drawing = mediapipe.solutions.drawing_utils
mp_drawing_styles = mediapipe.solutions.drawing_styles

hands_detector = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = "./data"

data = [] 
labels = []

for dir in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir)):
        
        data_temp = []
        
        x_ = []
        y_ = []
        
        image = cv2.imread(os.path.join(DATA_DIR, dir, img_path))
        image_to_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        result = hands_detector.process(image_to_rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_temp.append(x - min(x_))
                    data_temp.append(y - min(y_))
                    
            data.append(data_temp)
            labels.append(dir)
            
file_handler = open("dataset.pickle", "wb")
pickle.dump({"data": data, "labels": labels}, file_handler)
file_handler.close()
