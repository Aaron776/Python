# Para conectarse a la base de datos postgres debemos instalar la liberia psycopg2 con el comando (pip install psycopg2)
import cursor as cursor
import psycopg2
try:
    conexionPG = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1725159683Aron", # esta es la calve de min postgres
        database="Universidad"
    )
    print("Conexion exitosa")

    # Aqui solamente estoy obteniendo la vertsion de mi postgres
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


except:
    print ("Error en la conexion")