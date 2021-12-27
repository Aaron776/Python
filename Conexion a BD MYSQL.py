#Para conectar python a mysql debemos importar la liberia mysql_connector mediante el comando:  mysql-connector-python
import mysql.connector
try:
    conexion=mysql.connector.connect(user='root',
                                 password='',
                                 host='localhost',
                                 database='unibe',
                                 port='3306')
    print("Conexion exitosa")
except:
    print("Conexxion fallida")
