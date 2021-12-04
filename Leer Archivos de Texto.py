#Para leer un archivo de texto en python debemos poner el modo r o r+ dentro del parentesis
# Para poder leer un archivos de texto existen varios metodos en python
estudiante=open("Estudiantes.txt","r")

#Metodo readable() este metodo nos dice si el archivo que queremos leer es leible o no es
print(estudiante.readable())

#Metodo readline(): este metodo permite leer el archivo de texto linea por linea, si queremos leer la primera linea hacemos un print y si queremos ir leyendo las otras lienas vamos haciendo prints
print(estudiante.readline())

#Metodo readlines(): este metodo nos devuelve un array con todo lo escrito en el archivo
print(estudiante.readlines())
#print(estudiante.readlines()[1]) como nos devuele un arreglo podemos acceder a cada linea como si fuera una pisicon de un arreglo

# Metodo read(): este metodo permite tambien permite leer todo el archivo en la
print(estudiante.read())



estudiante.close()
