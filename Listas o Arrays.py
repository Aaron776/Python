#Listas o Arreglos: son estructura de datos, las listas se ponen entrecorchetes
lista=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(lista)

#Si queremos mostrar un unico elemento de la lista, los elementos de una lista se contabilizan desde el indice 0
print(lista[2])

#Python nos permite recorrer un eelento de la lista de atras hacia adelante y viceversa, si ponemos en negativo quiere decir que recorre desde el ultimo elemento hasta el principio
print(lista[-3])

#Podemos trabajr con sublistas tambien o con rangos(desde un elemento hasta otro)
print(lista[0:4])
print(lista[1:4])

#Listas dentro una lista
lista2=[1,2,3,4,[4.1,4.3,4.2],5]
print(lista2)
