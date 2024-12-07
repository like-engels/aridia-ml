from aridia_foundation.classes import AridiaPlaygroundDefinition
from aridia_growth.services import AridiaDatasetService


class CreateDatasetPlayground(AridiaPlaygroundDefinition):
    def __init__(self, dataset_dir: str) -> None:
        self.__DDIRR = dataset_dir

    def run(self):
        raw_data, raw_labels = AridiaDatasetService.load_raw_data(dir=self.__DDIRR)
        AridiaDatasetService.save_dataset(data=raw_data, labels=raw_labels)
