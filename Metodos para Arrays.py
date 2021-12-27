# Para acceder a un elemento de una lista lo hacemos mediante su posicion dentro de un entrecorchetes
lista=[1,2,3,4,"Jose"]
print(lista[4])

#Tambien opdemos acceder a un elemento usando numero negativos como indices y este recorrera la lista de fin a inicio
print(lista[-3])

#Podemos acceder tambien a un rango de elementos de la lista poniendo en los corchetes de que poisicon a que posicion queremos obtener los elementos de
lista2=[0,7,8.9,"Aaron",11,23,"true"]
print(lista2[1:4])

# Para recorrer una lista podemos hacerlo con un formato
nombres=["Aaron","Jose","Pedro"]
for item in nombres:
    print("Los nombres de la lista son: ",item)

#Metodo append():pemite añadir elementos a una lista, en el aprentesis ponemos el elemento que queremos agregar a la lista
lista3=[1,2,3,4]
lista3.append(34)
print(lista3)

#Concatenar listas
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6,66,77]
nueva_lista = lista_1 + lista_2
print(nueva_lista)

#Metodo del= permite elinar un eleneto o varios de una lista especificando el indice de ese elemento a eliminar el elemento
list=[9,3,6,10]
del list[2]
print(list)

# Metodo len : permite obtener la longitud o cantidad de elemento que tiene la lista
vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales))

#Saber si un elemento esta dentro de una lista usando un if y el operador in
vocales1 = ['a', 'e', 'i', 'o', 'u']
if "a" in vocales1:
    print("Si esta en la lista")
else:
    print("No esta dentro de la lista")

# Metodo sort():permite ordenar los elementos de una lista en orden ascendente
numbers=[10,9,2,4,0,3]
numbers.sort()
print(numbers)

# Metodo reverse():Obtiene los elementos de la lista en orden inverso.
lista4=[1,2,3,4,"Raul"]
lista4.reverse()
print(lista4)

# El método pop() elimina y retorna el ultimo elemento de una lista o especificando el elemento mediante su posicion o indice.
ciudades = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco']

print ("Ciudad removida : ", ciudades.pop() )
print ( "La ciudad en el indice 2 es : ", ciudades.pop(2) )