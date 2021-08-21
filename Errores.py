#Hay diferentes tipos de errores en Python
# Para tratar esos errores usamoslo siguiente: else,try, except,finally

#Uso del try(intentar) y del except
try: #aqui estamos diciendo que intente ejecutar estas lineas de codigo y si no puede hacerlo no lo va hacer y se iria al except
    num1=int(input("Digite un numero: "))
    print(num1)
except: # aqui dice que si hay una exepcion haria otra cosa que se le detalle
    print("Entrada invalida porque deves ingresar un numero entero")



#Uso del else y finally junto con los otros dos
try:
    numero1=float(input("Digita un numero: "))
    numero2=0
    print(numero1//numero2)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Entrada invalida,debe ingresar un entero")
else:
    print("No hubo ningun error")


