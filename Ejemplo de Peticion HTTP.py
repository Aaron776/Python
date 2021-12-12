import requests
url = 'http://httpbin.org/get'
r=requests.get(url)
data=r.json()
print(data)
print(data["origin"])