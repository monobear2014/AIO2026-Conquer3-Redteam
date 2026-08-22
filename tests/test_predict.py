import numpy as np

from src.predict import predict
from src.train import train_model


def test_predict_returns_correct_format():
    X = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
    y = np.array([0, 1, 1, 0])
    model = train_model(X, y)

    preds = predict(model, X)

    assert len(preds) == len(X)
    assert set(preds).issubset({0, 1})
