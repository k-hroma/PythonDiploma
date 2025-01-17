print('*** Regresar una tupla de valores desde una función ***')


# Definicion de la funcion


def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

# Programa principal


nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')
variable_tupla = nombre, apellido, edad
variable_lista = list(variable_tupla)
print(f"Convertir tupla: {variable_tupla} a lista: {variable_lista}")
