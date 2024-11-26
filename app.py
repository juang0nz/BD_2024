from flask import Flask, request, jsonify
from db.init_db import get_db_connection

app = Flask(__name__)
#RUTAS PARA ALTA, BAJA Y MODIFICACIÓN DE INSTRUCTORES
#PARA CREAR:
@app.route('/instructores', methods=['POST'])
def add_instructor():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Instructores (ci, nombre, apellido) VALUES (%s, %s, %s)',
        (data['ci'], data['nombre'], data['apellido'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Se agregó un instructor correctamente!"}), 201

#PARA ACTUALIZAR INSTRUCTORES:
@app.route('/instructores/<ci>', methods=['PUT'])
def update_instructor(ci):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Instructores SET nombre=%s, apellido=%s WHERE ci=%s",
        (data['nombre'], data['apellido'], ci)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Se actualizó un instructor correctamente!"})

#PARA ELIMINAR INSTRUCTORES:
@app.route('/instructores/<ci>', methods=['DELETE'])
def delete_instructor(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Instructores WHERE ci=%s", (ci,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Se eliminó un instructor correctamente!"})

#RUTAS PARA ALTA, BAJA Y MODIFICACIÓN DE TURNOS

#PARA CREAR UN NUEVO TURNO:

@app.route('/turnos', methods=['POST'])
def add_turno():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Turnos (hora_inicio, hora_fin) VALUES (%s, %s)",
        (data['hora_inicio'], data['hora_fin'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Turno creado exitosamente!"}), 201

# PARA ACTUALIZAR UN TURNO;
@app.route('/turnos/<id>', methods=['PUT'])
def update_turno(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Turnos SET hora_inicio=%s, hora_fin=%s WHERE id=%s",
        (data['hora_inicio'], data['hora_fin'], id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Turno actualizado con éxito!"})

#ELIMINAR UN TURNO:
@app.route('/turnos/<id>', methods=['DELETE'])
def delete_turno(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM BD.Turnos WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Turno eliminado con éxito!"})

#RUTA PARA MODIFICACIÓN DE ACTIVIDADES:

#ACTUALIZAR ACTIVIDADES:

@app.route('/actividades/<id>', methods=['PUT'])
def update_actividad(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE BD.Actividades SET descripcion=%s, costo=%s, res_edad=%s WHERE id=%s",
        (data['descripcion'], data['costo'], data['restriccion_edad'], id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Actividad actualizada!"})

#ALTA BAJA Y MODIFICACIONES DE ALUMNOS:



#PARA CREAR UN ALUMNO:

@app.route('/alumnos', methods=['POST'])
def add_alumno():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO BD.Alumnos (ci, nombre, apellido, fecha_nacimiento, telefono_contacto, correo) VALUES (%s, %s, %s, %s, %s, %s)",
        (data['ci'], data['nombre'], data['apellido'], data['fecha_nacimiento'], data['telefono'], data['correo_electronico'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Se creó un alumno nuevo!"}), 201


#SE ACTUALIZA UN ALUMNO:

@app.route('/alumnos/<ci>', methods=['PUT'])
def update_alumno(ci):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE BD.Alumnos SET nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono_contacto=%s, correo=%s WHERE ci=%s",
        (data['nombre'], data['apellido'], data['fecha_nacimiento'], data['telefono'], data['correo_electronico'], ci)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno ACTUALIZADO!"})

#PARA ELIMINAR ALUMNOS:

@app.route('/alumnos/<ci>', methods=['DELETE'])
def delete_alumno(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM BD.Alumnos WHERE ci=%s", (ci,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno ELIMINADO!"})

#PARA LAS CLASES:

#PARA CREAR UNA CLASE:

@app.route('/clases', methods=['POST'])
def add_clase():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (%s, %s, %s, %s)",
        (data['ci_instructor'], data['id_actividad'], data['id_turno'], False)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Se creó una nueva clase!"}), 201

#ACTUALIZACIÓN DE CLASE:

@app.route('/clases/<id>', methods=['PUT'])
def update_clase(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Clase SET ci_instructor=%s, id_actividad=%s, id_turno=%s WHERE id=%s",
        (data['ci_instructor'], data['id_actividad'], data['id_turno'], id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Clase ACTUALIZADA!"})

#SI QUIERO AGREGAR UN ALUMNO A UNA CLASE :

@app.route('/clases/<id_clase>/alumnos', methods=['POST'])
def add_alumno_clase(id_clase):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (%s, %s, %s)",
        (id_clase, data['ci_alumno'], data.get('id_equipamiento'))
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno agregado a la clase de forma exitosa!"}), 201

# PARA QUITAR ALUMNO DE LA CLASE:

@app.route('/clases/<id_clase>/alumnos/<ci_alumno>', methods=['DELETE'])
def remove_alumno_clase(id_clase, ci_alumno):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM BD.Alumno_clase WHERE id_clase=%s AND ci_alumno=%s",
        (id_clase, ci_alumno)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno eliminado de la clase!"})

# QUERYS QUE SE PEDIAN:
#EL REPORTE DE ACTIVIDADES QUE MAS INGRESOS GENERAN:

@app.route('/reportes/actividades/ingresos', methods=['GET'])
def reporte_ingresos_actividades():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT a.descripcion, SUM(c.costo + IFNULL(e.costo, 0)) AS ingresos_totales "
        "FROM Clase c "
        "JOIN BD.Actividades a ON c.id_actividad = a.id "
        "LEFT JOIN BD.Alumno_clase ac ON c.id = ac.id_clase "
        "LEFT JOIN Equipamiento e ON ac.id_equipamiento = e.id "
        "GROUP BY a.descripcion"
    )
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(resultados)

#REPORTE DE ACTIVIDADES CON MAS ALUMNOS:

@app.route('/reportes/actividades/alumnos', methods=['GET'])
def reporte_alumnos_actividades():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT a.descripcion, COUNT(ac.ci_alumno) AS cantidad_alumnos "
        "FROM BD.Actividades a "
        "JOIN BD.Clase c ON a.id = c.id_actividad "
        "LEFT JOIN BD.Alumno_clase ac ON c.id = ac.id_clase "
        "GROUP BY a.descripcion"
    )
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(resultados)

#REPORTE DE TURNOS CON MAS CLASES DICTADAS:

@app.route('/reportes/turnos/clases', methods=['GET'])
def reporte_clases_turnos():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT t.hora_inicio, t.hora_fin, COUNT(c.id) AS cantidad_clases FROM Turnos t  JOIN Clase c ON t.id = c.id_turno GROUP BY t.hora_inicio, t.hora_fin"

    )
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(resultados)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Escuela Deportes Nieve!"


if __name__ == '__main__':
    app.run(debug=True)
