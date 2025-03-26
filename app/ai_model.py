import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "safe_to_delete_model.joblib")

# Train a model to predict if a customer is safe to delete
def train_ai_model():
    data = {
        'last_contact_days': np.random.randint(0, 365, 1000),
        'contract_status': np.random.choice(['active', 'inactive', 'cancelled'], 1000),
        'data_sensitivity': np.random.choice(['high', 'medium', 'low'], 1000),
        'safe_to_delete': np.random.choice([0, 1], 1000),
    }
    df = pd.DataFrame(data)
    
    le_contract = LabelEncoder()
    le_sensitivity = LabelEncoder()
    df['contract_status'] = le_contract.fit_transform(df['contract_status'])
    df['data_sensitivity'] = le_sensitivity.fit_transform(df['data_sensitivity'])
    
    X = df[['last_contact_days', 'contract_status', 'data_sensitivity']]
    y = df['safe_to_delete']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, "/safe_to_delete_model.joblib")
    print(f"Model saved at {MODEL_PATH}")

def predict_safe_to_delete(last_contact_days, contract_status, data_sensitivity):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please train the model first.")
    
    model = joblib.load(MODEL_PATH)
    
    le_contract = LabelEncoder()
    le_sensitivity = LabelEncoder()
    
    encoded_contract_status = le_contract.fit_transform([contract_status])[0]
    encoded_data_sensitivity = le_sensitivity.fit_transform([data_sensitivity])[0]
    
    prediction = model.predict([[last_contact_days, encoded_contract_status, encoded_data_sensitivity]])
    return prediction[0] == 1
