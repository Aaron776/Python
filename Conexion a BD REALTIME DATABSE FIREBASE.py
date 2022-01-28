from firebase import firebase
def conexioFB():

       #Conexion a Firebase
       database=firebase.FirebaseApplication("https://aplicacion-a6a11-default-rtdb.firebaseio.com/",None)

       # Ingreso de datos a la Coleccion
       registros=[{'ci':'1725159683','nombre':'Aaron','apellido':'Ortiz','edad':25},
       {'ci':'1945159009','nombre':'Rosario','apellido':'Alban','edad':30},
       {'ci':'1724459663','nombre':'Dagmar','apellido':'Moya','edad':20},
       {'ci':'1123166775','nombre':'Camila','apellido':'Carillo','edad':22}]
       resultado=database.post("Usuarios",registros)

       # Mostrar Registros de la Coleccion
       mostrar=database.get("Usuarios",'')
       print (mostrar)

conexioFB()