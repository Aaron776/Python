#Los diccionarios son tambien una coleccion o arreglos en donde se gaurdan los datos de forma desordenada  y su caracteristica principal es que tienen dos elementos por posicion que son la
# la clave (las claves puede ser del tipo String o Numericas) y el valor ambos separtados por dos puntos(:), las claves no pueden ser reptidas o duplicadas
#Los dicionarios se usan las llaves({})

diccionario={"rojo":"red","azul":"blue","blanco":"white"}
print(diccionario)

#Si quiere saber el valor de un elemento debo buscarlo por  la clave ya no por el indice
print(diccionario["azul"])
print(diccionario["rojo"])

#Agregar elementos al diccionario
diccionario["amarillo"]="yellow"
print(diccionario)

#Modificar datos en el diccionario
diccionario["azul"]="BLUE"
print(diccionario)

#Eliminar datos en el diccionario con el metodo del() y dentro del parentesis ponemos  el nombre del elemento que queremos eliminar
del (diccionario["rojo"])
print(diccionario)

#Un diciconario vale poner cualquier tipo de datos, podemos poner listas o tuplas dentro de los dicionario
diccionario1={"Alejandor":[22,1.80],"Aaron":[24,1.96],"Jose":[22,1.67]}
print(diccionario1)

diccionario2={"Alejandro":{"edad":22,"estatura":1.80},"Aaron":{"edad":24,"estatura":1.96},"Jose":{"edad":22,"estaura":1.67}}
print(diccionario2["Aaron"])