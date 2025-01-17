"""
enteros --> inmutables
strings --> inmutables
listas  --> mutables
diccionarios --> mutables
"""

persona1 = ["Pepe Pedro", "Perez", 4, "12345678", "30000"]
print(persona1)
persona2 = ["Anna", "Perez", 12, "12345622", "43000"]
print(persona2)
persona3 = ["Josefa", "Rodriguez", 4, "12345563", "50000"]
print(persona3)
personas = [persona1, persona2]
print(personas)
personas.append(persona3)
# append=agregar otra variable
print(personas)
print("---" * 23)
print(personas[2] * 2)

empleados = []
# extend=agregar más de un elemento a la vez
empleados.extend([persona1, persona2])
print(empleados)
# de persona 1 el elemento 0 (Pepe)
# split: en este caso donde hay un espacio en blanco
print(persona1[0].split()[0])
