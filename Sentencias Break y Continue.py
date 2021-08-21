# La sentencia break y continue permiten manejar el flujo de informacion  dentro de un bucle
# y nos permite especificar que queremos cortar el bucle o saltar una de las iteraciones o mas de
# una la que nosotros elijamos

for indice in range(11):
    if indice==4:
        break #Aqui digo que cuando el indice tenga una valor de cuatro se corte el bucle
    print(indice)



dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for i in dias:
    if i=="Miercoles":
        continue  #Aqui digo que cuando el indice tenga una valor un cierto valor del arreglo se salte o no muestre ese valor y muestre los otros que siguen
    print(i)
