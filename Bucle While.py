#Un bucle while nos permite ejecutar una accion repetidas veces mientras una condicion no se cumpla

import  math
#Este import sirve para acceder a las funciones matematicas
numero=int(input("Digite un numero:"))
while numero<0:
    print("Se debe ingresar un numero positivo")
    numero = int(input("Digite un numero:"))

print(math.sqrt(numero)) #Para sacar la razi cuadrada de un numero se usa el metodo math.sqrt() y dentro del parentesis ponemos el valor


#En los bucles se usan una variable iteradora
i=0

while i<10:
    print("Hola Mundo")
    i+=1


i2=1
while i2<=10:
    print(i2)
    i2 += 1