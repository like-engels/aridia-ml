from typing import Literal

import typer
from aridia_foundation.classes import AridiaASLDefinitions
from playgrounds import CreateDatasetPlayground, DataCollectionPlayground, RunSampleAppPlayground, TrainDataPlayground

typer_app = typer.Typer()

SUPPORTED_LANGS = Literal["en_US", "es_NI", "en_NI"]


@typer_app.command()
def collect_data(lang_code: str = "en_US"):
    if lang_code not in SUPPORTED_LANGS.__args__:
        raise Exception("Invalid language code or not supported yet")

    playground = DataCollectionPlayground(language=AridiaASLDefinitions())
    playground.run()


@typer_app.command()
def create_dataset():
    playground = CreateDatasetPlayground(dataset_dir="./output_data")
    playground.run()


@typer_app.command()
def train():
    playground = TrainDataPlayground()
    playground.run()


@typer_app.command()
def run(lang_code: str = "en_US"):
    if lang_code not in SUPPORTED_LANGS.__args__:
        raise Exception("Invalid language code or not supported yet")

    playground = RunSampleAppPlayground()
    playground.run()


if __name__ == "__main__":
    typer_app()
