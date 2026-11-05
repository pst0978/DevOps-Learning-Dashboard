import json

#config.json file ko read mode me kholna
with open('config.json', "r") as file:
    data = json.load(file)

#pytjon dictionary. banne ke baad values ko accees karna
print("---Server Configuratin Laoded---")
print(f"Ennvironment: {data['environment']}")
print(f"Server status: {data['server_status']}")
print(f"Max Users Allowed: {data['max_users']}")    