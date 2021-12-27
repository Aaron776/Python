#En python para definir una lcase o crearla usamos la palabra class y ponemos el nombre seguido de dos puntos
#luego de definirla debemos inicializarla dentro de esa misma clase con la palabra def __init__(self)
# y dentro del self poenmos los atributos o propiedades que va a tener esa clase
#luego ponemos la palabra self otra vez con el nombre de esa propiedad y le igualamos con ese mismo nombre y esto es para
#inicializar esa variables o propiedades

class Estudiante:
    #Atributos de la Clase
    nombre=""
    apellido=""
    ci=""

    def __init__(self,ci,nombre,apellido,celular): #aqui creamos un constructor para inicializar la clase solo si queremos
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular

    #Metodos o Funciones de la Clase
    def saludar(self): # cuando creamos una funcion en una clase debemos poner la palabra self en los parentesis para especificar que vamos a trabajr con los atributos de esa clase
        print("Hola Mundo")
        print("Hola como estas:", self.nombre)

#Para crear un objeto de esa clase creada lo hacemos de la siguiente manera: ponemos el nombre de nuestro objeto y le igualamos a la clase que creamos
estudiante1=Estudiante(1725159683,"Aaron","Ortiz","0984588833")
print(estudiante1.ci)
estudiante1.saludar()

#Para poder cambiar un dato de mi objeto creado lo hacemos asi:
estudiante1.nombre="Patricio"
print(estudiante1.nombre)

