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




