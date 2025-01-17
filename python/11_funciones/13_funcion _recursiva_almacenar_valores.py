# Función recursiva pasando una lista como parámetro

def funcion_recursiva(numero, lista):
    # Caso base
    if numero == 1:
        lista.append(numero)  # Agregar el valor 1 a la lista
    # Caso recursivo
    else:
        funcion_recursiva(numero - 1, lista)  # Llamar recursivamente con numero - 1
        lista.append(numero)  # Agregar el valor actual a la lista

# Programa principal
resultados = []  # Lista vacía para almacenar los resultados
funcion_recursiva(5, resultados)

print(resultados)
# Salida: [1, 2, 3, 4, 5]

print('*** Imprimir del 1 al 5 de forma recursiva y almacenamiento en diccionario***')


# Función recursiva pasando un diccionario como parámetro

def funcion_recursiva(numero, diccionario):
    # Caso base
    if numero == 1:
        diccionario.update({numero: numero ** 2})  # Agregar clave y valor al diccionario
    # Caso recursivo
    else:
        funcion_recursiva(numero - 1, diccionario)  # Llamada recursiva
        diccionario[numero] = numero ** 2  # Agregar clave y valor al diccionario

# Programa principal
resultados = {}  # Diccionario vacío para almacenar los resultados
funcion_recursiva(5, resultados)

print(resultados)
# Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
Pasar un diccionario como argumento:

Se pasa un diccionario vacío (resultados = {}) a la función.
Este diccionario se actualiza en cada llamada recursiva.
Agregar claves y valores al diccionario:

En el caso base, el número 1 se agrega como clave y su cuadrado como valor (diccionario[numero] = numero ** 2).
En el caso recursivo, después de completar la llamada a funcion_recursiva(numero - 1, diccionario), se agrega el valor correspondiente al número actual.
"""