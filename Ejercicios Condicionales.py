#Escribir un programa que almacene la cadena de caracteres contraseña en una variable
# , pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable sin tener
# en cuenta mayúsculas y minúsculas.

contraseña="contraseña"
palabra=input("Digite la contraseña: ").lower()
if palabra==contraseña:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas son diferentes")


#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.
dividendo=float(input("Digite el valor: "))
divisor=float(input("Digite el valor: "))
if divisor==0:
     print("Error")
else:
    division=dividendo/divisor
    print("El resultado es: ",division)


# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero=int(input("Digite el numero: "))
if numero%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
