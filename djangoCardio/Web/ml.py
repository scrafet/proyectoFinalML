import joblib

model_in_disk = joblib.load('')

def predict(features):
    prediction = model_in_disk.predict(features)
    return prediction.tolist()