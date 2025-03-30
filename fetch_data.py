from Sql_connect import get_connection

def fetch_query_results(query):
    """Executes the given SQL query and returns the results."""
    connection = get_connection()
    if connection is None:
        return []
    
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error executing query:", e)
        return []
    finally:
        cursor.close()
        connection.close()
