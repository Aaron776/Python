import os #El módulo os de Python  permite  realizar operaciones dependiente del Sistema Operativo como crear una carpeta, listar contenidos de una carpeta, conocer acerca de un proceso, finalizar un proceso, etc.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
def conexion():
    archivo = os.path.join('firebase.json') # aqui me conecto con el servicio mediante el archivo json que vendrias hacer la llave de mi proyecto y de mi base de datos
    credenciales = credentials.Certificate(archivo) #aqui importo las credenciales
    try:
        firebase_admin.initialize_app(credenciales) # aqui inicializo la app
        backend = firestore.client()
    except:
        backend = firestore.client()

    db = backend
    usuarios= 'mHNBy9lJ2WiLH0HZpMjF'
    doc_ref = db.collection(u'usuarios').document(usuarios) #aqui llamo a mi coleccion mediante su id y su nombre
    doc = doc_ref.get()

    for i in doc.to_dict():
        print(doc.to_dict()[i])

conexion()