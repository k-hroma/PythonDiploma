# En Python, muchas estructuras de datos pueden desempaquetarse utilizando
# la sintaxis de desempaquetado (* o **) o asignación múltiple.
# Estas estructuras incluyen:


# #### 1. Listas y Tuplas
# Puedes desempaquetar valores directamente en variables:
lista = [1, 2, 3]
a, b, c = lista  # a=1, b=2, c=3

tupla = (4, 5, 6)
x, y, z = tupla  # x=4, y=5, z=6

# También puedes usar * para capturar valores restantes:
lista = [1, 2, 3, 4, 5]
a, *b, c = lista  # a=1, b=[2, 3, 4], c=5

# #### 2. Sets
# Aunque los conjuntos no son ordenados, puedes desempaquetarlos:
conjunto = {7, 8, 9}
a, b, c = conjunto  # El orden no está garantizado


# #### 3. Diccionarios
# Claves por defecto:
diccionario = {'x': 10, 'y': 20, 'z': 30}
a, b, c = diccionario  # a='x', b='y', c='z'

# Valores usando .values():
valores = diccionario.values()
a, b, c = valores  # a=10, b=20, c=30

# Claves y valores como tuplas con .items():
items = diccionario.items()
for clave, valor in items:
    print(clave, valor)


# #### 4. Cadenas
# Las cadenas se pueden desempaquetar carácter por carácter:
cadena = "abc"
a, b, c = cadena  # a='a', b='b', c='c'


# #### 5. Generadores e Iteradores
# Cualquier objeto iterable puede desempaquetarse:
generador = (x for x in range(3))
a, b, c = generador  # a=0, b=1, c=2


# #### 6. Clases Personalizadas
# Si defines un método __iter__ o __getitem__, 
# puedes hacer que tu clase soporte desempaquetado:
class MiClase:
    def __init__(self):
        self.datos = [1, 2, 3]

    def __iter__(self):
        return iter(self.datos)


obj = MiClase()
a, b, c = obj  # a=1, b=2, c=3


# #### 7. Desempaquetado Extendido
# Usando * para listas y ** para diccionarios:

# Para listas
lista1 = [1, 2, 3]
lista2 = [4, 5]
nueva_lista = [*lista1, *lista2]  # [1, 2, 3, 4, 5]

# Para diccionarios
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3}
nuevo_dic = {**dic1, **dic2}  # {'a': 1, 'b': 2, 'c': 3}
