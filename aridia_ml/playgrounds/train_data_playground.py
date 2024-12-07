import numpy as np
from aridia_foundation.classes import AridiaPlaygroundDefinition
from aridia_foundation.services import AridiaTrainingService
from aridia_growth.services import AridiaDatasetService


class TrainDataPlayground(AridiaPlaygroundDefinition):
    def run(self):
        dataset = AridiaDatasetService.load_dataset()

        labels = np.asarray(dataset["labels"])

        # data_shape = 2160

        # padded_data = [seq + [0] * (data_shape - len(seq)) for seq in dataset["data"] if len(seq) < data_shape]
        # truncated_data = [seq[:data_shape] for seq in dataset["data"] if len(dataset["data"]) > data_shape]

        # uniform_data = padded_data + truncated_data

        data = np.asarray(dataset["data"], dtype=np.float64)

        AridiaTrainingService.train_model(data=data, labels=labels)
