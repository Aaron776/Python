"""La serializacion es el proceso de convertir un objeto en una secuencia de bytes para almacenarlo
o transmitirlo a la memoria, para serializar en python usamos la liberia o modulo "Pickle"
"""
import pickle

#1. Serializar colecciones
lista=["Lunes","Martes","Miercoles","Jueves"]
archivo_serializado=open("lista","wb") #Creamos un archivo para seralizarlo
pickle.dump(lista,archivo_serializado) #con este metodo dum() lo que hacemos que que todo los elementos del arreglo se serialicen, dentro del parentesis poenmos el nombre de la lista y luego ponemos en donde queremos serializarlo(tiene que ser un archivo)

archivo_serializado.close()
del archivo_serializado

archivo=open("lista","rb")
lista_archivos=pickle.load(archivo) #con este metodo load() nos permite recuperar la lista para que deje de estar seralizada
print(lista_archivos)
