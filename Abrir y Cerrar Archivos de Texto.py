#Para abrir archivos de texto en Python o¿poenmos la plabara open() y ponemos entre las llaves el nombre del archivo
# y luego poenmos el tipo de tratamiento o el modo ( read, write,append,a,r+) y todo esto debemos guardarlo en una variable
# pero solo si esta en la misma carpeta de python, si es otro archivo debemos poner la ruta


estudiante=open("Estudiantes.txt","w")

#Para leer archivos usamos la funcion readable() para saber si podemos o no leer y luego usamos  read() para ahora si poder leer el archivo
print(estudiante.readable()) # antes de esto se debe poner dentro del open el modo r o r+ caso contrario no se puede hacer

print(estudiante.read())

print(estudiante.readline()) #esta funcion readline() lo que hace es devolvernos la primera linea del archivo de texto

print(estudiante.readlines())# esta funcion readlines() lo que hace es devolvernos como una lista lo que dice el archivo y podemos trabajar con un for
for est in estudiante:
    print(est)


#Para escribir archivos de texto debemos cambiar el modo en el open() por la w
print(estudiante.writable())

print(estudiante.write("Este es un nuevo archivo"))#con esta funcion write() en el parentesis poenmos el texto qu queremos insertar en el archivo pero borrara el anterior

#Para poder agregar datos o informacion a un archivo sin borrar lo anterior primero debemos poner en el open() el modo a
print(estudiante.write("Ahora no se cambia nada"))


#Para borrar archivos usamos debemos importar el modulo os y usamos el metodo remove() y entre parentesis ponemos el nombre del archivo
import os
os.remove("Estudiantes1.txt")


#Para cerra el archivo usamos la funcion close()
estudiante.close()