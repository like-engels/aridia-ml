from typing import Iterator, Tuple

import cv2
from cv2 import VideoCapture
from cv2.typing import MatLike


class AridiaVideocaptureService:
    @classmethod
    def initialize_service(cls, capture_device: int = 0):
        cls.__CAPTURE_DEVICE = VideoCapture(index=capture_device)

    @classmethod
    def release_camera(cls):
        capture_device_buffer = cls.__CAPTURE_DEVICE

        if not capture_device_buffer:
            raise Exception("Videocapture service hasn't been initialized yet")

        capture_device_buffer.release()
        cv2.destroyAllWindows()

    @classmethod
    def stream_data_from_camera(cls) -> Iterator[Tuple[bool, MatLike]]:
        capture_device_buffer = cls.__CAPTURE_DEVICE

        if not capture_device_buffer:
            raise Exception("Videocapture service hasn't been initialized yet")

        while True:
            if capture_device_buffer.isOpened():
                ret, frame = capture_device_buffer.read()
                yield ret, frame
            else:
                break

    @classmethod
    def get_snapshot(cls) -> tuple[bool, MatLike]:
        capture_device_buffer = cls.__CAPTURE_DEVICE

        if not capture_device_buffer:
            raise Exception("Videocapture service hasn't been initialized yet")

        ret, frame = capture_device_buffer.read()
        return ret, frame
