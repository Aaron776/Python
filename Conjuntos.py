#Los conjuntos son una collecion en donde los elementos donde se agregan elementos de forma desordenada y no npuede haber elementos repetidos ypara eso se usa el metodo set()
conjunto=set()
conjunto={1.3,2,"Jose"}
print(conjunto)

#Para agregar un elemento a un conjunto usamos el metodo add() y entre parentesis ponemos el elemento que queremos agregar
conjunto1=set()
conjunto1={1.3,2,"Jose"}
conjunto1.add("Raul")
conjunto1.add(0)
print(conjunto1)

#Eliminar elementos de un conjunto con el metodo discard() y entre parentesis ponemos el elemento que queremos eliminar
conjunto2=set()
conjunto2={1.3,2,"Jose"}
conjunto2.discard("Jose")
print(conjunto2)

#Para poder vaciar un conjunto usamos el metodo clear()
conjunto3=set()
conjunto3={1.3,2,"Jose"}
conjunto3.clear()
print(conjunto3)

#Buscar si un elemento  esta en el conjunto con el in
conjunto4=set()
conjunto4={1.3,2,"Jose"}
print(2 in conjunto4)