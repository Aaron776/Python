#Metodo replace(): este metodo permite reemplazar una palabra por otra dentro de una cadena, en el parentesis ponemos primero la palabra que sera reemplazada y luego ponemos la palabra por la cual vamos a reemplzar
from Variables import palabra

saludo="Hola Como estas"
resultado=saludo.replace("estas","te fue")
print(resultado)

# Metodo join(): este metodo permite unir o poner dentro de una cadena un elemento que nosotos querramos, primero ponemos entre comillas el elemento que queremos unir u luego va el join() y en el parentesis  ponemos el string o la cadena a la cual vamos a unir
sal="Hola Jose"
resultado1=":".join(sal)
print(resultado1)

#Metodo find(): este metodo permite buscar una palabra dentro de un caracter y si la encuntra nos devuelve su posicion en donde esta y si no la encuentra devuelve un -1, este metodo toma en cuenta mayusculas y minusculas asi como tildes
cadena="Pepe se fue al rio"
print(cadena.find("rio"))

#Metodo split(): este metodo permite dividir una cadena de caracteres mediante un separador como dos puntos, punto y coma o comillas
cadena1="Pepe se fue a jugar"
print(cadena1.split(" "))

#Metodo capitalize(): este metodo nos devuleve una cadena o un a plabar con el primer caracter en mayusculas
nombre="raul"
print(nombre.capitalize())

#Metodo upper(): este metodo nos devuleve una cadena o un a plabar todo en mayusculas
nombre1="jose"
print(nombre1.upper())

#Metodo lower(): este metodo nos devuleve una cadena o un a plabar todo en minusculas
apellido="ORTIZ"
print(apellido.lower())

# Metodo startswith() : indican si la cadena en cuestión comienza con el conjunto de caracteres pasados como argumento, y retornan True o False en función de ello.
palabra="Buen dia Mario"
print(palabra.startswith("Buen"))

# Metodo endswith():indica si la cadena en cuestión termina con el conjunto de caracteres pasados como argumento, y retornan True o False en función de ello.
palabra1="Hoy jugaste bien"
print(palabra1.endswith("jugaste"))

# Metodo count(): retorna el número de veces que se repite un conjunto de caracteres especificado.
oracion="Aaron es buen estudiante en informatica y es buen jugador"
print(oracion.count("buen"))

