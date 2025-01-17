import sys
# Acceso a argumentos de líneas de comando:

# python modulo_sys.py 1, 2, 3, "hola mundo"

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv)
print(type(sys.argv))
print(len(sys.argv))
print(sys.argv[1:])

"""
resultado:
1,
2,
3,
hola
['modulo_sys.py', '1,', '2,', '3,', 'hola mundo']
<class 'list'>
5
['1,', '2,', '3,', 'hola']
"""

# Puedes redirigir el flujo de entrada estándar (sys.stdin), salida estándar\n
# (sys.stdout) y error estándar (sys.stderr).
sys.stdout.write("Esto se imprime en la consola\n")
"""resultado:
Esto se imprime en la consola
"""

# Acceso a información del intérprete:
print("Versión:", sys.version)
print("Plataforma:", sys.platform)

"""
Versión: 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
Plataforma: win32
"""

# Gestión de excepciones:
sys.exc_info()

# Finalización del programa:
sys.exit("¡Terminado!")

# Modificación de la ruta de búsqueda de módulos:
print(sys.path)  # Muestra las rutas de búsqueda actuales
