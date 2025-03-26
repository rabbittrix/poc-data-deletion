import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="insurance_db",
        user="postgres",
        password="postgres",
        host="postgres", 
        port=5432
    )
    
def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, policy_number, is_deleted FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return customers

def soft_delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET is_deleted = TRUE WHERE id = %s", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
def hard_delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()