from sklearn.ensemble import IsolationForest
import pandas as pd

model = IsolationForest(contamination=0.02)

def detect_anomaly(data):

    df = pd.DataFrame([data])

    prediction = model.fit_predict(df)

    return int(prediction[0])