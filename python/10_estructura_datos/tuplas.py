"""*** Manejo de Tuplas ***"""

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modificar una tupla
# mi_tupla[0] = 10
# mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# Crear una tupla para una coordenada x,y
coordenadas = (3, 5)

# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidada = (1, (2, 3), (4, 5))
print(f'Segundo elemento tupla anidada: {tuplas_anidada[1]}')

"""*** Desempaquetado de Tuplas ***"""

# unpacking
producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')

"""*** Combinación de Listas y Tuplas ***"""

# definir una lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total

precio_total = 0

print('Información de los productos: ')
for producto in productos:
    # print(producto)
    id, descripcion, precio = producto
    # unpacking
    print(
      f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio  # producto[2]
print(f'Precio total de los productos: ${precio_total}')
