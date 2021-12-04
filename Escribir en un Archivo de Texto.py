#Para poder escribir en un archivo ponemos el modo "w" o usamos el metodo "a" de append para agregar las cosas
estudiante=open("Estudiantes.txt","a")

#Metodo writetable(): nos dice si en el archivo se puede escribir o no
print(estudiante.writable())

#Metodo write(): este metodo permite agreagr texto a nuestro archivo
print(estudiante.write("\nHola Aaron")) # en el print nos sale el numero de caracteres que agregamos al archivo

#Metodo

estudiante.close()