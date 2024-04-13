import json

file_name = "data.json"

with open(file_name) as data:
    datos = json.load(data)
print(datos["ip"] , print(datos["so"]), datos["hostname"], print(datos["version"][0]), print(datos["cpu"]))