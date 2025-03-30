import mysql.connector

def get_connection():
    """Establish and return a MySQL database connection."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="PythonTasks@1234",
            database="company_db"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
