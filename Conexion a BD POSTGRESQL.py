# Para conectarse a la base de datos postgres debemos instalar la liberia psycopg2 con el comando (pip install psycopg2)
import cursor as cursor
import psycopg2
try:
    conexionPG = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1725159683Aron", # esta es la calve de mi postgres
        database="Universidad"
    )
    print("Conexion exitosa")

    # Aqui solamente estoy obteniendo la version de mi postgres
    cursor=conexionPG.cursor()
    cursor.execute("SELECT version()")
    fila=cursor.fetchone()
    print(fila)

    # Para realizar una consulta en postgres mediante python usamos el metodo cursor() y usando el metodo execute() dentro de los parentesis ponemos el nombre la consulta que queremos hacer
    cursor = conexionPG.cursor()
    cursor.execute("SELECT * FROM estudiante")
    registros=cursor.fetchall()  # usamos el metodo fetchall() para obtener todos los rgistros de una tabla y el metodo fecthone() es para obtener un solo registro de la tabla
    for item in registros:     #para imprimir los registro de una tabla usamo un for in
        print(item)

    # Insertar datos o registros a la base de datos
    cursor = conexionPG.cursor()
    codigo = int(input("Ingresar codigo del alumno: "))
    cedula = input("Ingresar cedula: ")
    nombres = input("Ingresar nombres: ")
    apellidos = input("Ingresar apellidos: ")
    telefono = input("Ingresar telefono: ")
    sentencia="INSERT INTO alumnos (codigo,cedula,nombres,apellidos) VALUES({0},'{1}','{2}','{3}','{4}')".format(codigo,cedula,nombres,apellidos,telefono)
    cursor.execute(sentencia)
    conexionPG.commit()
    print("Registro de datos exitoso")

except:
    print ("Error en la conexion")