#Las cadenas de texto  son e si arreglos de caracteres y estas cadenas son inmutables
cadena="Hola Mundo"

#Si queremos acceder a un caracter de esa cadena lo hacemos de las mims a forma en la que trabajamos con los arrays
letra=cadena[0] #entre las llevaes ponemos el indice del valor que queremos obtener
print(letra)
letra1=cadena[-2]
print(letra1)

#Tambien podemos extraer una parte de la cadena igual que en una lista
letras=cadena[0:4] #entre los corchetes poenmos de que indice a que indice queremos que imprima la cadena de texto
print(letras)

#Para poder unir valores numericos a cadenas de texto es usar la funcion str() para tranformar el numero en cadena de texto
numero=200
union= "En el colegio hay "+str(numero)+ " alumnos dispuestos a estudiar"
print(union)

#La funcion format() pemite hacer lo mismo que lo anterior
numero1=100
cadena="En el colegio hay {} dispuestos a estudiar" .format(numero1) # en los parentesis ponemos la variable que queremos poner en la cadena y ponemos unas lleves en el sitio donde  va a esatr esa variable
print(cadena)
