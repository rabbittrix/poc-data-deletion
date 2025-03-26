# Project Structure

    poc-data-deletion/
    ├── app/  # Streamlit Core Code
    │   ├── __init__.py
    │   ├── main.py  # Interface Streamlit
    │   ├── data_deletion.py  # Data deletion logic
    │   ├── ai_model.py  # AI Model for Predictive Analytics
    │   ├── Dockerfile
    │   └── requirements.txt  # Python Dependencies
    ├── airflow/
    │   └── dags/
    │       └── data_deletion_pipeline.py  # Airflow DAG   
    ├── .env
    ├── init-db.sql
    ├── safe_to_delete_model.joblib
    ├── train.py
    ├── docker-compose.yml  # Docker Configuration for PostgreSQL, Streamlit and Airflow
    └── README.md

Another architecture being delivered.
