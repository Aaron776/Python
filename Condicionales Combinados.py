#Condicionales combinados o anidados con Operadores logicos
#Un condiconal anidado es un condicional dentro de otro
edad=int(input("Digite su edad:"))
if edad>0:
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("Edad incorrecta")

#Condicionales con Valores Logicos ( and,or,not)
numero=int(input("Digite un numero: "))
if numero>0 and numero<100:
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("Edad incorrecta")



