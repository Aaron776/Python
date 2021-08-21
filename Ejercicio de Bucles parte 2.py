#Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i)

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
# que dura la inversión.
amount = float(input("¿Cantidad a invertir?:  "))
interest = float(input("¿Interés porcentual anual?:  "))
years = int(input("¿Años?: "))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount)))

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")



#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña="contraseña"
palabra=input("Digite la contraseña: ").upper().lower()
while palabra!=contraseña:
    palabra=input("Vuelva a digitar la xontraseña: ")
print("Las contraseñas coinciden")


#Escribir un programa que pida al usuario una palabra y luego muestre
# por pantalla una a una las letras de la palabra introducida empezando por la última.
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
