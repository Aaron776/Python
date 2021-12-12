import requests
def peticionesHttp():
    url=("https://pokeapi.co/api/v2/pokemon-form/")
    r=requests.get(url)
    print(r)     #Con este print lo que hago es imprimir el resultado de mi peticioon Http si es exitosa o no y esto me devuelve un response
    if r.status_code == 200:
        data=r.json()
        print(data)     #Con este print estoy imprimiendo todo lo que me llega de mi servicio como formato json que en python es un diccionario
        for item in data["results"]:   #En este for simplemento esto recorriendo el atributo "results" que contiene un arreglo de objetos y estoy imprimiendo los valores del atributo name de ese esos objetos
            print(item["name"])

peticionesHttp()
