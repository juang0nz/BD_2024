from mysql.connector import connect, Error

def get_db_connection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="root",
            database="BD"
        )
        return connection
    except Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
