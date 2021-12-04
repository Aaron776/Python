#Para las interfaces graficas usamos el modulo TKinte y algunos componentes son los siquientes:
"""
tik: Es el contenedor de todos los elementos (widgets)  que tendra nuestra intgerfaz, ademas es al que llamaremos raiz o root.su tamaño puede definirse o ser modificada

Frame: Frame o marco es por si mismo  un widget aunwue no nos permita interactuar con el programa, el marco sera el contenedor de los
widgets que utilizaremos

Label: Es un widget en que podremos mostrar textos estaticos

Entry: Cuadros de texto para ingresar textos cortos (una sola linea)

Text: Este widget nos pemite escribir textos largos (multilinea)

Button: Es un boton con texto

Radiobutton

CheckButton

Menu: Son los tipicos botones que vemos en las ventanas en la parte superior qu despliegan opciones

Dialogs: Ventanas emergentes que muestran informacion al usuario como alertas o ventanas para elegir archivos, etc.

"""
#Importamos la biblioteca Tkinter
from tkinter import *

#Creamos las raiz o root de nuestra app y le damos culquier nombre
root=Tk()
#Añadimos un titulo a la ventana
root.title("Aaron Ortiz")
#Añadimos un icono para Windows
root.iconbitmap("python_18894.ico")
#Decimos si nuestro root quiere ser redimensioable o no con 0 y  1 o con true o false, aqui simplemente es ajustar el tamaño de la ventana
root.resizable(1,1)
#Definir el ancho y el alto de la interfaz
root.geometry("600x300")
#Cambiar algunas opciones
root.config(bg="blue")

#Vamos hacer un frame hijo de la raiz
frame=Frame(root)

#Empaquetar nuestro frame dentro de la raiz
frame.pack()

#Cambiamos el color de fondo de nuestro marco
frame.config(bg="red")
#Darle un tamaño a nuestro frame
frame.config(width=600,height=300)
#Cambiar el cursor del raton, darle un estilo al borde y un tamaño
frame.config(cursor="circle")
frame.config(relief="sunken") #o groove
frame.config(bd=30)
#Posicionamente del marco frame
frame.pack(side=RIGHT,anchor=N)
#HACER QUE EL FRAME OCUPE DISTINTOS TAMAOS EN EL ROOT (redimensionar)
frame.pack(fill=BOTH,expand=1)
#Ejecutamos el bucle infinito
root.mainloop() #el bucle infinito vas siempre al final de nuestro programa, este bucle pasa escuando los eventos que vayas desatando