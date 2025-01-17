print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
print(f'Diccionario de persona: {persona}')

# Creamos un dict usando el constructor dict()
mi_diccionario = dict(nombre="Juan", edad=30, ciudad="Madrid")
print(mi_diccionario)

# Acceder a los elementos del diccionario
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")
print(f"Ciudad: {persona.get('ciudad')}")


