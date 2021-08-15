#Las tuplas son otro tipo de listas pero con la difrencia que estas son listas inmutables o que no pueden modificarse
tupla=(4,6,"Aaron",0.9)
print(tupla)

#Una accion que puedes hacer en las duplas es buscar un elemento con cualquiera de los metodos antres visto

print(tupla[1])
print(tupla[0:3])
print(tupla.count(6))

#Podemos tranformar las tuplas en listas normales con el metodo list()
tupla=(4,6,"Aaron",0.9)
lista=list(tupla)
print(lista)

#Podemos tranformar las listas en tuplas con el metodo tuple()
lista1=[1,4,6,7,"Patricio"]
tupla1=tuple(lista1)
print(tupla1)

