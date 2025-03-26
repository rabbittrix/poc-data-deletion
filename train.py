import sys
import os
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.ai_model import train_ai_model, predict_safe_to_delete

def train_ai_model():
    data = pd.DataFrame({
        "feature1": [1, 0, 1, 0],
        "feature2": [0, 1, 0, 1],
        "label": [1, 0, 1, 0]
    })
    model = RandomForestClassifier()
    model.fit(data.drop(columns=['label']), data['label'])
    joblib.dump(model, "safe_to_delete_model.joblib")

result = predict_safe_to_delete(last_contact_days=300, contract_status="inactive", data_sensitivity="low")
print("Safe to Delete:", result)

if __name__ == "__main__":
    train_ai_model()