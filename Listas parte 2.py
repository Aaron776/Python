#Funcion lent permite determinar cuanto elementos tiene la lista
lista3=[1,2,3,4,[4.1,4.3,4.2],5]
print(len(lista3))

#Agregar o instertar elemento a una lista con la funcion append
lista4=[1,2,3,4,5]
lista4.append(6)
lista4.append("Aaron")
print(lista4)

#Agregar elemento a una lista en una posicion indicada con la funcion insert y se le debe pasar parametros: la posicion y el elemento que queremos agregar
lista5=[1,2,4,5]
lista5.insert(2,3)
print(lista5)

#Agregar varios elementos de golpe a una lista
lista6=[0,2,4,5]
lista6.extend([10,11,12])
print(lista6)

#Concatenar listas
lista7=[0,1,2]
lista8=[3,7]
lista9=lista7+lista8
print(lista9)

#Saber si un elemento esta en una lista con la funcion (in) dentro del print y esto me devuleve un True o False
lista10=[0,1,2,"Patricio"]
print("Patricio"in lista10)
print(4 in lista10)

#Como saber en que indice se encuntra un elemento usando el metodo index y a este se le pasa el valor que queremos buscar
lista11=[0,1,2,"Dagmar"]
print(lista11.index("Dagmar"))

#Para determinar cuantos valores hay repetidos en una lista se usa el metodo count
lista12=[0,1,2,0]
print(lista12.count(0))

#Como eliminar el ultimo elemento de una lista con el metodo pop() y si queremos indicarle un elemento especifico del arreglo en el parentesis debemos poner el indice del elemento que queremos eliminar
lista13=[9,10,2,1]
lista13.pop()
print(lista13)

#Para eliminar un elemento de una lista pero sin que yo sepa el indice del valor en donde esta mi elemento uso el metodo remove() y entre el parentesis pongo el elemento que quiero eliminar

lista14=[9,10,2,1]
lista14.remove(2)
print(lista14)

#Para eliminar todos los elementos de una lista se usa el metodo clear()
lista15=[0,0,0]
lista15.clear()
print(lista15)

#Para dar vuelta una lista se usa el metodo reverse()
lista16=[1,2,3]
lista16.reverse()
print(lista16)

# Hacer que dentro d euna lista un elemento se copie las veces que quieras usando el operador artmetico de la multiplicacion
lista17=[1,2,3,4]*3
print(lista17)

#Para ordernar los elementos de una lista de forma ascendente con el metodo sort()
lista18=[8,10,20,0]
lista18.sort()
print(lista18)

#Para ordernar los elementos de una lista de forma descendente con el metodo sort() pero dentro del parentesis ponemos el metodo reverse e igualando a True
lista19=[8,10,20,0]
lista19.sort(reverse=True)
print(lista19)

#Cambiar el valor del eleneto de una lista por otro valor, ponemos el nombre la lista y entre llaves pones el indice del valor que queremos cambiar
lista20=[8,10,20,0]
lista20[1]=9
print(lista20)




