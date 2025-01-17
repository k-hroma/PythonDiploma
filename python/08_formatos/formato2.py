import pprint

anna = {
    "identificacion": {"nombre": "Anna", "apellido": "Rodríguez"},
    "edad": 50,
    "sueldo": 30000,
}
josefa = {
    "identificacion": {"nombre": "Josefa", "apellido": "Rodríguez"},
    "edad": 70,
    "sueldo": 60000,
}

print(anna, josefa)  # es muy dificl de encontrar

db = {}
db["anna"] = anna
db["josefa"] = josefa
print(db)
print("---" * 23)
pprint.pprint(db)
db = [anna] + [josefa]
pprint.pprint(db)