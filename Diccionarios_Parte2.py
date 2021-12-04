equipo={23:"Paula Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",9:"Alvaro Morata",1:"Alex Sandro",13:"Andrea Pirlo"}

#Imprimir todo el Diccionario
print(equipo)

#Mostrar un elemento del diccionario mediante su llave
print(equipo[23])

#Usando el metodo get() en un diccionario lo que nos permite es imprimir un mensaje cuando busquemos un elemento que no existe en el diccionario
print(equipo.get(10,"No existe este jugador en este diccionario"))

#Buscar en nuestro diccionario un elemento con el metodo in y te devuelve un true o un false
print(10 in equipo)

#Mostrar solo las claves del diciconario con el metodo keys()
print(equipo.keys())

#Mostrar solo los valores de lo elemento del diccionario con el metodo values()
print(equipo.values())

#Mostrar la clave y el nombre del elemento con el metodo items() (el metodo items se usa para recorrer diccionarios)
print(equipo.items())

#Mostrar la cantidad de elementos que hay en un diccionario con el metodo len()
print(len(equipo))

#Limpiar el diciconario con el metodo clear()
equipo.clear()
print(equipo)