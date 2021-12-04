#Usamos el metodo append para agregar cada elemento al archivo json que se crea
import json
data = {} # creamos el objeto json como si fuera un diccionario
data['clientes'] = []

data['clientes'].append({
    'Nombre': 'Sigrid',
    'Apellido': 'Mannock',
    'Edad': 27
    })

data['clientes'].append({
    'Nombre': 'Joe',
    'Apellido': 'Hinners',
    'Edad': 31
    })

data['clientes'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open('clientes.json', 'w') as file: # en el parentesis ponemos el nombre del archivo json que se va a crearusamos aqui el modo w para escribir en el archivo Json
    json.dump(data, file, indent=4) #usamoe el metodo jump() y en el aprentesis ponemos el nombre del diciionario que sera tranformado a objeto Json y el ident es opcional solo para que se vea bien el archivo

