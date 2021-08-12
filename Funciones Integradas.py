# Estas funciones sirven para hacer conversiones entre tipos de datos

#Conversion de un valor numerico a una cadena de texto
n=str(10)
m=str(10.7)

#Convertir un valor entero a un valor binario
a=bin(20)
print(a)

#Convertir un valor entero a un valor hexadecimal
b=hex(20)
print(b)

#Convertir cualquier valor a entero por ejemplo uno binario
c=int("0b10100",2)
print(c)

#Convertir cualquier valor a entero por ejemplo uno hexadecimal
d=int("0x14",16)
print(d)

#Valor absoluto
e=abs(-80)
print(e)

#Redondear un numero
d=round(2.6)
print(d)

#Funcion len que me cuenta cuantos caracteres tiene mi cadena de texto
nombre=len("Aron Ortiz")
print(nombre)
