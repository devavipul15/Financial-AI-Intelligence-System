import pandas as pd

def predict_transaction(data):

    df = pd.DataFrame([data])

    amount = df["amount"][0]

    risk_score = min((amount / 10000) * 100, 99)

    fraud_prediction = 1 if amount > 7000 else 0

    return {
        "fraud_prediction": fraud_prediction,
        "risk_score": round(risk_score, 2)
    }