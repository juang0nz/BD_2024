from flask import Flask, request, jsonify
from db.init_db import get_db_connection

app = Flask(__name__)

@app.route('/instructores', methods=['POST'])
def add_instructor():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)",
        (data['ci'], data['nombre'], data['apellido'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Instructor added successfully!"}), 201
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Escuela Deportes Nieve!"


if __name__ == '__main__':
    app.run(debug=True)
