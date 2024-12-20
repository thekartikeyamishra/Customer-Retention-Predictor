import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


def save_model(model, path="models/churn_model.pkl"):
    joblib.dump(model, path)


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)
