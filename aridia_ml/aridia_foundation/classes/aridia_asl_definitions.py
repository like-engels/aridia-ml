from .aridia_language_definitions import AridiaLanguageDefinitions, AridiaSignType


class AridiaASLDefinitions(AridiaLanguageDefinitions):
    @classmethod
    def fetch_definitions(cls) -> dict[str, AridiaSignType]:
        return {
            "a": AridiaSignType.FIXED,
            "b": AridiaSignType.FIXED,
            "c": AridiaSignType.FIXED,
            "d": AridiaSignType.FIXED,
            "e": AridiaSignType.FIXED,
            "f": AridiaSignType.FIXED,
            "g": AridiaSignType.FIXED,
            "h": AridiaSignType.FIXED,
            "i": AridiaSignType.MOVEMENT,
            "j": AridiaSignType.FIXED,
            "k": AridiaSignType.FIXED,
            "l": AridiaSignType.FIXED,
            "m": AridiaSignType.FIXED,
            "n": AridiaSignType.FIXED,
            "o": AridiaSignType.FIXED,
            "p": AridiaSignType.FIXED,
            "q": AridiaSignType.FIXED,
            "r": AridiaSignType.FIXED,
            "s": AridiaSignType.FIXED,
            "t": AridiaSignType.FIXED,
            "u": AridiaSignType.FIXED,
            "v": AridiaSignType.FIXED,
            "w": AridiaSignType.FIXED,
            "x": AridiaSignType.FIXED,
            "y": AridiaSignType.FIXED,
            "z": AridiaSignType.MOVEMENT,
        }
