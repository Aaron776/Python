equipo={23:"Paula Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",9:"Alvaro Morata"}
print(equipo)
print(equipo[23])

#Usando el metodo get() en un diccionario lo que nos permite es imprimir un mensaje cuando busquemos un elemento que no existe en el diccionario
print(equipo.get(10,"No existe este jugador en este diccionario"))

#Buscar en nuestro diccionario con el metodo in y te devuelve un true o un false
print(10 in equipo)

#Mostrar solo las claves del diciconario con el metodo keys()
print(equipo.keys())

#Mostrar solo los nombres de lo elemento del diciconario con el metodo values()
print(equipo.values())

#Mostrar la clave y el nombre del elemento con el metodo items() (el metodo items se usa para recorrer diccionarios)
print(equipo.items())

#Mostrar la cantidad de elementos que hay en un diccionario con el metodo len()
print(len(equipo))

#Limpiar el diciconario con el metodo clear()
equipo.clear()
print(equipo)