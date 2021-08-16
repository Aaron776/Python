#Las pilas son una estructura de datos del tipo lifo(ultimo en entrar y primero en salir)
#una pila se crea como una lista o un arreglo
pila=[1,2,3]

#Agregar elemento al final con el metodo append() y en el parentesis ponemos el elemento que queremos agregar
pila.append(4)
print(pila)

#Sacar elementos por el final usando el elemnto pop()
pila.pop()
print(pila)

#El elemnto pop permite retornar el valor que estas quitando pero para eso debes guardarlo en otra variable
n=pila.pop()
print(n)