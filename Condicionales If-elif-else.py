#Condicionales
#Sentencia If-Else: Aqui en vez de abrir llaves al final ponemos dos puntos(:) y tampoco ponemos parentesis, todas las intrucciones de un if deben tener la misma tabulacion caso contrario el programa detectara que ya no forma parte d eun if
numero=int(input("Digite un numero:"))
if numero>0:
    print("El numero es positivo")
#Sentencia elif es para encadenar varias condiciones, en otros lenguajes se usa el else-if
elif numero==0:
    print("El numero es cero")
else:
    print("El numero no es positivo")







