#Para abrir archivos de texto en Python o¿poenmos la plabara open() y ponemos entre las llaves el nombre del archivo
# y luego poenmos el tipo de tratamiento o el modo ( read, write,append,a,r+) y todo esto debemos guardarlo en una variable
# pero solo si esta en la misma carpeta de python, si el archivo que queremos abrir esta en otra carpeta o en otra parte de nuestra compu debemos poner la ruta de donde se encuentra ese archivo


estudiante=open("Estudiantes.txt","r+") # el modo r+ permite leer y escribir el archivo
print(estudiante) # hacemos un print para saber en que modo esta nuestro archivo


#Para cerra el archivo usamos la funcion close()
estudiante.close()