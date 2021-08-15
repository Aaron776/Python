#Para crear un conjunto usamos las llaves({}) pero si quieres hacer un conjunto vacio ahi si usamos el metodo set()
a={1,2,4,5}
b={5,7,8,9}
c={1,2,3,4,5}

#Como hacer la iguladad entre dos conjuntos
print(a==b)

#Metodo lent para saber cuantos elementos tienen los conjuntos
print(len(a))

                            #Operacion en Conjuntos
#Union de Conjuntos usnado el simbolo(|)
c=a|b
print(c)

#Interseccion entre conjuntos con el simbolo(&)
d=a&b
print(d)

#La diferencia entre conjuntos usando el simbolo aritmetico menos(-)
e=a-b
print(e)

#La diferencia simetrica son elementos que estan entre los conjuntos  pero que no estan entre ellos y se hace con el simbolo (^)
f=a^b
print(f)

#Como saber que un conjunto es un subconjunto de otro usando el metodo issubset() y me va  devolver un true o False
print(a.issubset(c))

#Como saber que un conjunto es un superconjunto de otro usando el metodo issuperset y me va  devolver un tru
print(a.issuperset(c))

#Saber si dos conjuntos son o no disconexos o sea que no comparten elementos en comun con el metodo isdisjoint()
print(a.isdisjoint(b))

#Conjuntos inmutables usando la funcion frozenset()
d=frozenset({1,2,3,4,5})
print(d)

