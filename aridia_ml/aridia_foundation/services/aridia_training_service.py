import os
import pickle

from numpy.typing import NDArray
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class AridiaTrainingService:
    @classmethod
    def train_model(cls, data: NDArray, labels: NDArray) -> None:
        x_train, x_test, y_train, y_test = train_test_split(
            data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=84
        )

        model = RandomForestClassifier(
            random_state=84,
            n_estimators=200,
            criterion="gini",
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            max_features="sqrt",
            bootstrap=True,
            oob_score=False,
            n_jobs=1,
            class_weight="balanced",
            verbose=0,
        )

        model.fit(x_train, y_train)

        y_predict = model.predict(x_test)

        score = accuracy_score(y_test, y_predict)

        print(f"{score * 100}% of samples were classified correctly!")

        if not os.path.exists("./output"):
            os.makedirs("./output")

        file_handler = open("./output/model.atm", "wb")
        pickle.dump({"model": model}, file_handler)
        file_handler.close()
