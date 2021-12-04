#Para usar objetos Json en python debemos imporat la liberia json en
#Para importar un archivo json usamons el metodo with open() en el parentesis ponemos el nombre del archivo si esta en la mimsa carpetao la ruta del archivo si esta en otro lado
import json
with open('paises.json') as file:
    paises = json.load(file) #creamos una variable donde vamos a guardarlos objetos de archivo json y usamos el metodo load()
print(paises) # con el print podemos ver todo el archivo json en forma de diccionario
print(paises[1]) # como es un diccionario o una lista podemos reccorer el obejto Json usando los indices de cada elemento

for i in paises: #aqui recorro el objeto Json con un for que tambie se puede hacer
    print("Nombre del Pais: ", i['nombre'])
    print("Nombre de la Capital : ", i['capital'])