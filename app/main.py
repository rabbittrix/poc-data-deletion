import streamlit as st
from data_deletion import get_all_customers, soft_delete_customer, hard_delete_customer
from ai_model import predict_safe_to_delete
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "safe_to_delete_model.joblib")

st.title("Insurance Data Deletion Dashboard")
st.write("Monitor and automate data deletion in compliance with regulations.")

customers = get_all_customers()
for customer in customers:
    customer_id, name, email, policy_number, is_deleted = customer
    if not is_deleted:
        st.write(f"Name: {name}, Email: {email}, Policy Number: {policy_number}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Soft Delete"):
                soft_delete_customer(customer_id)
                st.success(f"Customer {customer_id} marked for deletion.")
        with col2:
            if st.button("Hard Delete"):
                hard_delete_customer(customer_id)
                st.success(f"Customer {customer_id} permanently deleted.")
                
st.header("AI Prediction for Safe Deletion")
last_contact_days = st.number_input("Last Contract Days", min_value=0, max_value=365)
contract_status = st.selectbox("Contract Status", ["active", "inactive", "cancelled"])
data_sensitivity = st.selectbox("Data Sensitivity", ["high", "medium", "low"])

if st.button("Predict Safe to Delete"):
    safe_to_delete = predict_safe_to_delete(last_contact_days, contract_status, data_sensitivity)
    result = "Safe to Delete" if safe_to_delete else "Not Safe to Delete"
    st.write(f"Prediction: {result}")