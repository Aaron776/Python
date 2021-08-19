#Las funciones es un bloque de codigo que contiene un bloque de codigo que contiene instruccines
#Una funcion se declara con la plabra def y le damos un nombre luego onemos los parentesis y por ultimo ponemos dos puntos

def saludar():
    print("Hola usuario")  #todo el codigo de la funcion debe estar identadopara que lo reconozca que forma parte de esa funcion


#Para usar la funcion simplemente se la debe llamar de la siguiente forma: poenmos el nombre de la funicon con los dos parentesis
saludar()

#Los parametros son los datos o variables que les enviamos a esa funcion y van entre los parentesis
def saludo_usuario(nombre,edad):
    print("Hola usuario",nombre,"mucho gusto tienes",edad)


saludo_usuario("Aaron",23)

