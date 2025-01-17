# Metodos de cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')
mayusculas = cadena1.upper()  # convertir a mayusculas
print(f'Cadena en mayúsculas: {mayusculas}')
print(f'Cadena en minúsculas: {cadena1.lower()}') # convertir a minusculas
cadena2 = ' Juan Perez '
print(f'Cadena con espacios: {cadena2}')
print(f'Cadena sin espacios: {cadena2.strip()}') # eliminar espacios al inicio y al final

# probando
nombre = "rocio mendonca"
nombre = nombre.replace(" ", "")
print(nombre)
nombre = nombre.strip()
print(nombre)
nombre = nombre.split()
print(nombre)