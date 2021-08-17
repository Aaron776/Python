#Para tributar un determinado impuesto se debe ser mayor de 16 años
# y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
# muestre por pantalla si el usuario tiene que tributar o no.

edad=int(input("Digite su edad: "))
ingresos=float(input("Digite sus ingresos: "))
if edad>16 and ingresos>1000:
     print("Usted tiene que tributar")
else:
    print("Usted no puede tributar")


# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo
# al sexo y el nombre. El grupo A esta formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo
# B por el resto. Escribir un programa que
# pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre=input("Escriba su nombre: ").lower()
sexo=input("Escriba su sexo (M o F): ").lower()
if sexo=="f":
    if nombre<'m':
        print("Usted pertence al grupo A")
    else:
        print("Usted pertence al grupo B")

elif sexo=='m':
    if nombre>'n':
        print("Usted pertence al grupo A")
    else:
        print("Usted pertenece al grupo B")
else:
    print("Volver a intentar")



