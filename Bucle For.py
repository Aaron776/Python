#A este bucle for se le conoce por tener un numero determinado de iteraciones,es decir a priori vamos a saber cuantas veces se va a repetir
#  este bucle for se trabaja con listas o arreglos tambien con tuplas y conjuntos, tenemos un iterador que va a recorrer los elementos de esa lista
#La cantidad de elementos en la lista representa la cantidad de ciclos o la cantidad de veces que se van a repetir las instrucciones
for i in [1,2,3,4,5,"Aaron"]:
    print("Hola mundo")
    #para mostrar los elementos del arreglo
    print(i)

#El arreglo puede estar creado afuera del for tambien
coleccion=[0,0,4,12]
for i in coleccion:
    print("Hola Aaron")

#Tambien este bucle recorre cadenas de texto, aqui las instrucciones en el ciclo se van a repetir de acuerdo a la cantidad de letrtas de esa cadena
nombre="Aaron" #Aaron tiene 5 letras
for i in nombre:
    print("Que mas ve")


#Con el bucle for podemos definir la cantidad de veces que que se va ejecutar las intrucciones sin definir un arreglo
#usando la funcion range() y dentro del parentesis ponees la cantidad de ciclos que quieres que se ejecute esa intruccion
for i in range(10):
    print("Barcelona")


#Bucle for para imprimir letra por letra de una palabra o un string
for letra in "Academia":
    print(letra)

#Hay que entender que luego de la palabra for ponemos una variable que contendra la cantidad de iteraciones que tiene ese arreglo y que valor tiene esa iteracion
dias=["Lunes","Martes","Miercoles"]
for i in dias:
    print(i)
