#Estas expresiones nos pemiten trabajar con textos , mas especificamente para realizar busquedas de texto
#a traves de metodos y utilizando una sintaxis propia de la liberias  de expresiones regulares
#que utlicimemos en cada lenguaje

#Cuando usar:
#- Saber si existe una cadena de caracteres(palabras) dentro de una texto
#- Conocer cuantas veces se encuentra una cadena de caracteres dentro de un texto
#- Detectar si un texto se ajusta a un formato especifico

                                         #Tipos:
#Modulo re:Este metodo nos buscara la primera coincidencia de una cadena de caracteres dentro de un texto
#devolvera un objeto si es localizado o None si no es encontrado
import re
cadena="Hola Aaron"
print(re.search("Hola", cadena)) #usando este metodo debemos poner el parentesis primero la palabra que queremos buscar y luego ponemos la variable o arreglo en donde queremos buscar
#dentro de este metodo search() tenemos los metodos start() que devuelve la posicion o inidce de donde inicia la plabara y end() devuelve la posicion o indice en donde terminar la palabra
cadena2="joder"
if re.search("joder",cadena2):
    print("Se ha encontrado la palabra")
else:
    print("Esa cadena de caracteres no existe aqui")


#Metodo findall() del modulo re: este metodo devurleve una lista con las coincidencias encontradas
print(re.findall("joder",cadena2))# ademas este metodo puede trabajar con otras funciones como len

#Metodo split() del modulo re: Me separa una cadena por el caracter que yo le indique
print(re.split("o",cadena2))

#Metodo sub() del modulo re: Lo que pemite hacer es sustituir una palabra
print(re.sub("Aaron","desarrolladores",cadena)) # aqui en el parentesis ponemos el el parentesis la plabara que queremos reemplzar, luego ponemos la plabara por la cual queremos reemplzar y por ultimo ponemos en que lista o variable queremos hace rese cambio


#Metacaracteres
#Anclas(^,$,
lista=["Aaron:Primero","Jose:Segundo","Ramon:Tercero","Marcos:Cuarto"]
for palabra in lista:
    if re.findall('^Aar',palabra):   #Si uso el ^ lo que hace es buscar todos lo elementos que comienzen con
        print(palabra)               #Si uso el $ lo que hace es buscar los elementos  que finalicen con



#Rangos:Aqui especificacmos desde que rango de letras queremos realizar la busqueda
cadena3="De aqui a la luna"
print(re.findall("[a-e]",cadena3)) #para buscar con rangos usamos los corchetes y tambien usamos los numeros de posicion

#Rango Negado:Busque:todo lo que no esta en ese rango
print(re.findall("[^a-e]",cadena3))



