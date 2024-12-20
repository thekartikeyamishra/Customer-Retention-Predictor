import joblib


def load_model(path="models/churn_model.pkl"):
    return joblib.load(path)


def predict_churn(model, customer_data, scaler):
    customer_data_scaled = scaler.transform([customer_data])
    probability = model.predict_proba(customer_data_scaled)[0][1]
    return probability
