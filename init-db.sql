CREATE DATABASE insurance_db;
CREATE DATABASE airflow_db;

\c insurance_db;

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    policy_number TEXT UNIQUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS policies (
    id SERIAL PRIMARY KEY,
    policy_number TEXT UNIQUE NOT NULL,
    policy_type TEXT NOT NULL,
    policy_start_date DATE NOT NULL,
    policy_end_date DATE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS claims (
    id SERIAL PRIMARY KEY,
    claim_number TEXT UNIQUE NOT NULL,
    policy_number TEXT NOT NULL,
    claim_date DATE NOT NULL,
    claim_amount NUMERIC NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    payment_number TEXT UNIQUE NOT NULL,
    claim_number TEXT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount NUMERIC NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

\c airflow_db;

CREATE TABLE IF NOT EXISTS dags (
    id SERIAL PRIMARY KEY,
    dag_id TEXT UNIQUE NOT NULL,
    dag_name TEXT NOT NULL,
    dag_description TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    task_id TEXT UNIQUE NOT NULL,
    task_name TEXT NOT NULL,
    task_description TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instances (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT UNIQUE NOT NULL,
    task_id TEXT NOT NULL,
    dag_id TEXT NOT NULL,
    execution_date DATE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_dependencies (
    id SERIAL PRIMARY KEY,
    upstream_task_id TEXT NOT NULL,
    downstream_task_id TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_dependencies (
    id SERIAL PRIMARY KEY,
    upstream_task_instance_id TEXT NOT NULL,
    downstream_task_instance_id TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_logs (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT NOT NULL,
    log_date DATE NOT NULL,
    log_message TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_status (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT NOT NULL,
    status TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_results (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT NOT NULL,
    result TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_errors (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT NOT NULL,
    error_message TEXT NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS task_instance_retries (
    id SERIAL PRIMARY KEY,
    task_instance_id TEXT NOT NULL,
    retry_date DATE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

