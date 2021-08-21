#Escribir un programa en el que se pregunte al usuario por una frase y una letra
# ,y muestre por pantalla el número de veces que aparece la letra en la frase.

palabra=input("Digite una palabra: ").upper().lower()
letra=input("Digite una letra: ").upper().lower()
acum=0
for i in palabra:
    if i==letra:
      acum+=1
print("La cantidad de veces que se repite esa letra en su palabra es: ",acum," veces")


#Escribir un programa que muestre el eco de todo lo
#que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)