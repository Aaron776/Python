#Las funciones es un bloque de codigo que contiene un bloque de codigo que contiene instruccines
#Una funcion se declara con la plabra def y le damos un nombre luego onemos los parentesis y por ultimo ponemos dos puntos

def saludar():
    print("Hola usuario")  #todo el codigo de la funcion debe estar identado para que lo reconozca que forma parte de esa funcion


#Los parametros son los datos o variables que les enviamos a esa funcion y van entre los parentesis
def saludo_usuario(nombre,edad):
    print("Hola usuario",nombre,"mucho gusto tienes",edad)



#Ejemplo de Funciones
def mayorNumero(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

#Para usar la funcion simplemente se la debe llamar de la siguiente forma: poenmos el nombre de la funicon con los dos parentesis, en caso de tener argumentos la funcion cuando la llamemos en los parentesis debemos poner los datos que pide la funcion
saludar()
saludo_usuario("Aaron",23)
print(mayorNumero(4.2,5.6,5.7))



