import os

import cv2
from cv2.typing import MatLike


class AridiaFileService:
    DATA_DIR = "./output_data"

    @classmethod
    def save_images_to_dir(cls, image_set: dict[str, list[MatLike]]):
        print("Saving data to disk...")

        for letter in image_set:
            if not os.path.exists(os.path.join(cls.DATA_DIR, letter)):
                os.makedirs(os.path.join(cls.DATA_DIR, letter))

            letter_data = image_set[letter]

            for index, data in enumerate(letter_data):
                cv2.imwrite(os.path.join(cls.DATA_DIR, letter, f"{index}.jpg"), data)
