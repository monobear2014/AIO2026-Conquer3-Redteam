from sklearn.linear_model import LogisticRegression


def train_model(X, y):
    """Train a simple baseline Logistic Regression model."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model
