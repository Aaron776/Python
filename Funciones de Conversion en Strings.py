#Funcion lower para tranformar todos los caracteres a minuscula
letra=input("Ingrese letra:").lower()
if letra=='a':
    print("La letra es vocal")
else:
    print("La letra no es vocal")

#Funcion upper para tranformar todos los caracteres a mayuscula
letra1=input("Ingrese letra:").upper()
if letra1=='B':
    print("La letra es vocal")
else:
    print("La letra no es vocal")

#Funcion que devuelve una copia de la cadena con su primer carácter en mayúscula y el resto en minúsculas.
palabra="doctor"
modificada=palabra.capitalize()
print(modificada)

modificada1=palabra.casefold()
print(modificada1)

