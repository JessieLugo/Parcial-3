import requests

url = 'http://localhost:5000/system_info'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    #print("ip:", data['local'])
    #print("hostname:", data['hostname'])
    print(data)
else:
    print("Error al obtener la información del sistema:", response.status_code)