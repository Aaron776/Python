#Las colas son  uns estrutura de datos del tipo fifo(el primero en entrar es el primero en salir)
#
cola=["Maria","Jose","Aaron","Roberto"]
print(cola)

#Para agregar elementos a la cola al final con el metodo append()
cola.append("Dagmar")
print(cola)

#Sacar el primer elemento de la cola y asi sucesivamente con el metodo pop(0)
n=cola.pop(0)
print(n)
n=cola.pop(0)
print(n)