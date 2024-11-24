from mysql.connector import connect, Error

def get_db_connection():
    return connect(
        host="localhost",
        user="root",
        password="root",
        database="BD"
    )
