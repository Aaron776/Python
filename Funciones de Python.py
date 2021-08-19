                             #Funciones de Cadenas en python
#1) print()	Imprime en pantalla el argumento o variable. Ejemplo:
print("Hola")

#2) len()	Determina la longitud o cantidad de caracteres de una cadena.Ejemplo:
palabra="jugar"
print(len(palabra))

#3) join()	Convierte en cadena de textos una arreeglo o cualquier tipo que tengas separacion.Ejemplo
lista = ["Python", "es"]
listaConvertida='-'.join(lista)
print(listaConvertida)


#4) split()	Convierte una cadena con un separador a una lista o aaray.Ejemplo:
palabra1="Raul esta grande"
lista2=palabra1.split()
print(lista2)

#5) replace()	Reemplaza una cadena o una palabra por otra
palabra2="Aaron era mi amigo"
print (palabra2.replace('mi','nuestro')) #en el paretesis del replace ponemos primero la palabara la queremos reemplazar y luego con una
#coma alado ponemos la palabra que queremos que reemplazca

#6) upper()	Convierte una cadena en Mayúsculas. Ejemplo:
texto = "jhan franco"
print(texto.upper())

#7) lower()	Convierte una cadena en Minúsculas. Ejemplo:
texto2="DIA"
print(texto2.lower())

                                #FUNCIONES NUMERICAS
#1) range()	Crea una lista con un rango de números o elementos. Ejemplo:
x = range(5) #entre parentesis ponemos el numero maximo de elementos que contendra esa lista. tambien pueden ser tuplas o conjuntos
print(list(x))
print(tuple(x))

#2) max()	Determina el valor mas alto de entre un grupo de números
lista3=[0, 1, 2]

print (max(lista3))


#3) min()	Determina el menor valor de entre un grupo de números
x2 = [0, 1, 2]

print (min(x2))


#4) sum()	Suma el total de una lista de números
x3=[1,2,1]
print(sum(x3))

#5) round()	Redondea después de la coma de un decimal
numero=5.6
print(round(numero))
#6) type()	Devuelve el tipo de valor(si es int, float, string) de un elemento
tipo=22
print(type(tipo))