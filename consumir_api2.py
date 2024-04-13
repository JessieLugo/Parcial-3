import requests

#se requiere una url
url = "https://zelda.fanapis.com/api/games"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud Exitosa')
    print("Datos: ", data)
    

else:
    print("Error en la solicitud: ", response.text)
