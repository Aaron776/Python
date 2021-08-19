#Estas funciones son anonimas(no se les asigna un nombre) que se ejecutan en una linea
# es decir que solo pueden tener una expresion, estas funciones se almacenan en una varaible y despues del igual
#se debe poner la palabra lambda y poner los argumentos y poner dos puntos
resultado=lambda numero:numero+20
print(resultado(10))

suma=lambda numero1,numero2: numero1+numero2
print(suma(1,2))