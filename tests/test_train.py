import numpy as np

from src.train import train_model


def test_train_model_with_small_sample():
    X = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
    y = np.array([0, 1, 1, 0])

    model = train_model(X, y)

    assert hasattr(model, "predict")
    preds = model.predict(X)
    assert len(preds) == len(y)
