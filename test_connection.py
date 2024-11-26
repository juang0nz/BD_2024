from mysql.connector import connect, Error

def get_db_connection():
    try:
        connection = connect(
            host="localhost",       # Dirección del servidor
            user="root",            # Nombre de usuario
            password="root", # Contraseña del usuario
            database="BD"           # Nombre de la base de datos
        )
        return connection
    except Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

def test_connection():
    connection = get_db_connection()
    if connection and connection.is_connected():
        print("Conexión exitosa")
        connection.close()
        print("Conexión cerrada")
    else:
        print("No se pudo conectar a la base de datos")

if __name__ == "__main__":
    test_connection()
