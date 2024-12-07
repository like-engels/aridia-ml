from enum import Enum, auto
from typing import Protocol


class AridiaSignType(Enum):
    FIXED = auto()
    MOVEMENT = auto()
    GESTURE = auto()


class AridiaLanguageDefinitions(Protocol):
    @classmethod
    def fetch_definitions(cls) -> dict[str, AridiaSignType]: ...
