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

#  Métodos útiles

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'Diccionario de persona: {persona}')

# Actualizar un elemento existente
persona["nombre"] = "Rocio"
print(f"Diccionario de persona actualizado: {persona}")

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')
    print(llave, valor)
    tupla = llave, valor
    print(tupla)
    print(list(tupla))

# Obtener los valores
print(f'\nValores del diccionario: ')
for valor in persona.values():
    print(f'- Valor: {valor}')

# Obtener las llaves
print(f'Impresión de las llaves del diccionario:')
for llave in persona.keys():
    print(f'- {llave}')

# Devuelve un objeto de vista con las claves.
claves = persona.keys()   
print(type(claves))

# Devuelve un objeto de vista con los valores.
valores = persona.values()  
print(valores)

# Devuelve pares clave-valor como tuplas en un objeto de vista.
clave, valor = persona.items()  
print(clave, valor)
print(type(clave), type(valor))

items = persona.items()
print(items)
print(type(items))

# Obtiene el valor de una clave, devolviendo un valor por defecto si la clave no existe.
nombre = persona.get("nombre", "no especificada")  
print(nombre)

telefono = persona.get("teléfono", "no especificada")
print(telefono)

# Actualiza el diccionario con los pares clave-valor de otro.
print(persona)
nuevo_diccionario = {"profesion": "Ingeniero", "edad": 35}
persona.update(nuevo_diccionario)  

# Elimina una clave específica y devuelve su valor, o un valor por defecto si no existe.
nombre = persona.pop("nombre", "valor_por_defecto")  
print(persona)

print('*** Listas y Diccionarios ***')

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista:
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    print(f'Detalle: Nombre: {persona.get("nombre")}, Apellido: {persona.get("apellido")}')