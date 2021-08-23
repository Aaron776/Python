class Estudiante:
    def __init__(self,ci,nombre,apellido,celular):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular

    #Para crear una funcion en una clase en Python es con la palabra def seguida del nombre de esa funcion
    def mostrarNombre(self,nombre):
        print(nombre)

#Obejto de esta clase Estudiante()
estudiante1=Estudiante(1725159683,"Aaron","Ortiz","0984588833")
estudiante1.mostrarNombre("Roman")