import requests


url = 'http://localhost:1010/apertura/'


resp = requests.get(url=url)
data = resp.json()
print(data)

for dt in data:
    #print(dt['contrato'])
    if dt['contrato'] == 'prueba1':
        print(dt['acceso']) 
        print(dt['id'])
    