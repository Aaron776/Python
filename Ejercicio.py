#Encontrar el menor elemento y el mayor de una lista determinada por el usuario

cantidad=int(input("Digite la cantidad de valores que tendra la lista:"))
lista=[]
for x in range(cantidad):
    valor=int(input("Ingrese el valor: "))
    lista.append(valor)

#imprimimos la lista
print(lista)
print("El elemento mayor de la lista es: ",max(lista))
print("El elemento menor de la lista es: ",min(lista))


