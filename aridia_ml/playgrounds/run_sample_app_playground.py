import cv2
from aridia_foundation.classes import AridiaPlaygroundDefinition
from aridia_foundation.services import AridiaPredictionService
from aridia_growth.services.aridia_videocapture_service import AridiaVideocaptureService


class RunSampleAppPlayground(AridiaPlaygroundDefinition):
    def run(self):
        AridiaPredictionService.initialize_model()

        AridiaVideocaptureService.initialize_service()

        for ret, frame in AridiaVideocaptureService.stream_data_from_camera():
            H, W, _ = frame.shape

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            result = AridiaPredictionService.predict_snapshot(rgb_frame=frame_rgb)

            if result is not None:
                prediction, x_coords, y_cords = result

                x1 = int(min(x_coords) * W) - 10
                y1 = int(min(y_cords) * H) - 10

                x2 = int(max(x_coords) * W) - 10
                y2 = int(max(y_cords) * H) - 10

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, prediction, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
