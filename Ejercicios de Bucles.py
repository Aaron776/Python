#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra=input("Digite la palabra: ")
i=0
while i<10:
    print(palabra)
    i+=1


# Escribir un programa que pregunte al usuario su edad y muestre
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Digite su edad: "))
i=0
for i in range(edad):
    print("Tu edad es: ",str(i+1))

#Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero=int(input("Ingrese numero: "))
for i in range(1, numero+1, 2):
    print(i)





#Escribir un programa que permita al usuario ingresar una cantidad de numeros que el quiera y luego le muestre la suma
#la suma de todos esos numeros
cantidad=int(input("Cuantos numeros quiere ingresar: "))
i=0
acum=0
while i<cantidad:
    numero=int(input("Digite el valor: "))
    i+=1
    acum+=numero
print("las suma es: ",acum)


#Escriba un programa que pregunte cuantos numeros se van a introducir, permita el ingreso de dichos numeros
#y muestre en pantalla cuantos numero son pares y la suma de todos los impares
cantidad1=int(input("Cuantos numeros quiere ingresar: "))
acum_pares=0
acum_impares=0
for i in range(cantidad1):
     valor=int(input("Ingrese el valor: "))
     if valor%2==0:
         acum_pares+=1
     else:
         acum_impares+=valor

print("La cantidad de pares son: ",acum_pares)
print("La suma de los impares es: ",acum_impares)


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



