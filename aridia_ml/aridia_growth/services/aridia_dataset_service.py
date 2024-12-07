import os
import pickle
from typing import List, Tuple

import cv2
import mediapipe as mediapipe


class AridiaDatasetService:
    FIXED_SIZE = 42 * 2

    @classmethod
    def load_raw_data(cls, dir: str) -> Tuple[List[List[float]], List[str]]:
        data: List[List[float]] = []
        labels: List[str] = []

        mp_hands = mediapipe.solutions.hands

        hands_detector = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

        LANDMARK_SHAPES = set()

        for subdir in os.listdir(dir):
            for img_path in os.listdir(os.path.join(dir, subdir)):
                data_temp = []

                in_memory_image = cv2.imread(os.path.join(dir, subdir, img_path))
                image_to_rgb = cv2.cvtColor(in_memory_image, cv2.COLOR_BGR2RGB)

                mediapipe_result = hands_detector.process(image_to_rgb)

                if mediapipe_result.multi_hand_landmarks:
                    for hand_landmarks in mediapipe_result.multi_hand_landmarks:
                        # Extract all x and y coordinates
                        x_ = [landmark.x for landmark in hand_landmarks.landmark]
                        y_ = [landmark.y for landmark in hand_landmarks.landmark]

                        # Normalize and append data
                        min_x, min_y = min(x_), min(y_)
                        data_temp.extend(
                            [(landmark.x - min_x, landmark.y - min_y) for landmark in hand_landmarks.landmark]
                        )

                    flattened_data = [coord for pair in data_temp for coord in pair]
                    while len(flattened_data) < cls.FIXED_SIZE:
                        flattened_data.append(0.0)

                    flattened_data = flattened_data[: cls.FIXED_SIZE]

                    LANDMARK_SHAPES.add(len(flattened_data))

                    data.append(flattened_data)
                    labels.append(subdir)

        if len(data) <= 0 and len(labels) <= 0:
            raise Exception(
                "The data collection and label collection are empty. Please check if the collected data includes visible hands that can be processed."
            )

        [print(f"Landmark dataset shape found: {length}") for length in LANDMARK_SHAPES]

        return data, labels

    @classmethod
    def save_dataset(cls, data: List[List[float]], labels: List[str]) -> None:
        if not os.path.exists("./dataset"):
            os.makedirs("./dataset")

        file_handler = open("./dataset/output.adsd", "wb")
        pickle.dump({"data": data, "labels": labels}, file_handler)

        file_handler.close()

    @classmethod
    def load_dataset(cls) -> dict[str, List[List[float]]]:
        data_set = pickle.load(open("./dataset/output.adsd", "rb"))

        return data_set
