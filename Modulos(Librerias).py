


#Un moduloo es un archivo que podemos importar dentro de otro archivo en el cual estamos
#trabajando y hacer uso de su contenido como funciones o variables

#Para importar un modulo usamos la palabra import y luego colocamos el nombre del archivo que queremos importar
import Variables
print(Variables.suma)


#En cambio si solo queremos importar solo un parte del codigo del otro archivo poenmos la palabra from luego
#el nombre del archivo luego la palabra import y a lado poenmos el nombre o la parte que queremos importar
from Variables import suma
print(suma)