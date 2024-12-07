import os
import pickle
from typing import Tuple

import mediapipe
import numpy as np
from cv2.typing import MatLike
from sklearn.ensemble import RandomForestClassifier


class AridiaPredictionService:
    FIXED_SIZE = 42 * 2

    @classmethod
    def initialize_model(cls, model_dir: str = "./output/model.atm") -> None:
        if not os.path.exists(model_dir):
            raise Exception(f"There's no model available to load in dir: {model_dir}")

        file_handler = open(model_dir, "rb")
        model_data = pickle.load(file_handler)
        cls.__MODEL: RandomForestClassifier = model_data["model"]

        mp_hands = mediapipe.solutions.hands

        hands_detector = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        cls.__HANDS_DETECTOR = hands_detector

    @classmethod
    def predict_snapshot(cls, rgb_frame: MatLike) -> Tuple[str, list, list] | None:
        if not cls.__HANDS_DETECTOR or not cls.__MODEL:
            raise Exception("Prediction service hasn't been initialized")

        results = cls.__HANDS_DETECTOR.process(rgb_frame)

        if not results.multi_hand_landmarks:
            return None

        data_aux = []
        x_coords, y_coords = zip(
            *[
                (landmark.x, landmark.y)
                for hand_landmarks in results.multi_hand_landmarks
                for landmark in hand_landmarks.landmark
            ]
        )

        min_x, min_y = min(x_coords), min(y_coords)

        data_aux = [
            (landmark.x - min_x, landmark.y - min_y)
            for hand_landmarks in results.multi_hand_landmarks
            for landmark in hand_landmarks.landmark
        ]

        flattened_data = [coord for pair in data_aux for coord in pair]
        while len(flattened_data) < cls.FIXED_SIZE:
            flattened_data.append(0.0)

        prediction = cls.__MODEL.predict([np.asarray(flattened_data)])
        return prediction[0], x_coords, y_coords
