import cv2
from aridia_foundation.classes import AridiaLanguageDefinitions, AridiaPlaygroundDefinition
from aridia_growth.services import AridiaFileService, AridiaVideocaptureService
from cv2.typing import MatLike


class DataCollectionPlayground(AridiaPlaygroundDefinition):
    def __init__(self, language: AridiaLanguageDefinitions, dataset_size: int = 100) -> None:
        self.__LANG = language
        self.__DSIZE = dataset_size

    def run(self):
        language_alphabet = self.__LANG.fetch_definitions()
        collected_data: dict[str, list[MatLike]] = {}

        AridiaVideocaptureService.initialize_service()

        for letter in language_alphabet:
            for ret, preview_frame in AridiaVideocaptureService.stream_data_from_camera():
                cv2.putText(
                    preview_frame,
                    f'Ready? Press "{letter}"!',
                    (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.3,
                    (0, 255, 0),
                    3,
                    cv2.LINE_AA,
                )
                cv2.imshow("frame", preview_frame)
                if cv2.waitKey(25) == ord(letter):
                    break

            counter = 0
            for ret, frame in AridiaVideocaptureService.stream_data_from_camera():
                if counter < self.__DSIZE:
                    cv2.imshow("frame", frame)
                    cv2.waitKey(25)
                    collected_data.setdefault(letter, []).append(frame)
                    counter += 1
                else:
                    break

        AridiaVideocaptureService.release_camera()

        AridiaFileService.save_images_to_dir(image_set=collected_data)
