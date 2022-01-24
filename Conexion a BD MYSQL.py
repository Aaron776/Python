#Para conectar python a mysql debemos importar la liberia pymsql mediante el comando:  mysql-connector-python
import pymysql
try:
    conexionSQ=pymysql.connect(host='localhost', user='root',password='',db="sana")
    cursor=conexionSQ.cursor()
    print("Conexion Exitosa")

    # Aqui solamente estoy obteniendo la version de mi MYSQL
    cursor = conexionSQ.cursor()
    cursor.execute("SELECT version()")
    fila = cursor.fetchone()
    print(fila)

    # Para realizar una consulta en postgres mediante python usamos el metodo cursor() y usando el metodo execute() dentro de los parentesis ponemos el nombre la consulta que queremos hacer
    cursor = conexionSQ.cursor()
    cursor.execute("SELECT * FROM alumnos")
    registros = cursor.fetchall()  # usamos el metodo fetchall() para obtener todos los rgistros de una tabla y el metodo fecthone() es para obtener un solo registro de la tabla
    for item in registros:  # para imprimir los registro de una tabla usamo un for in
        print(item)

        # Insertar datos o registros a la base de datos
    cursor = conexionSQ.cursor()
    id_alumno = int(input("Ingresar id del alumno: "))
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    cursor.execute("INSERT INTO alumnos (id_alumno,nombre,apellido) VALUES(id_alumno,'nombre','apellido')")
    conexionSQ.commit()
    print("Registro de datos exitoso")
except:
    print("Error en la Conexion")


