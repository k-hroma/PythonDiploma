import os
"""
Importa el módulo os, que proporciona funciones para interactuar con el
sistema operativo.
Este módulo es útil para trabajar con rutas de archivos y directorios,
entre otras cosas.
"""
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
# os.path.abspath(file):
"""
Obtiene la ruta absoluta del archivo Python que se está ejecutando
actualmente.
"""
# os.path.dirname(...):
"""
Extrae el directorio que contiene el archivo, eliminando el nombre del
archivo.
"""
# BASE_DIR:
"""
Es una variable que almacena el directorio base donde se encuentra el
archivo en ejecución.
"""
ruta = os.path.join(BASE_DIR, "mascotas.jpg")
# os.path.join(...):
"""
Combina el directorio base (BASE_DIR) con los subdirectorios y
el nombre del archivo que se desea crear o utilizar.
En este caso, construye una ruta que apunta al archivo mascotas.jpg
en la carpeta img dentro del directorio base.
"""
# ruta: Es una variable que almacena esta ruta completa.
print(BASE_DIR)
print(ruta)

"""
En resumen, este código construye dinámicamente una ruta al archivo
mascotas.jpg en la carpeta img, garantizando que funcione en cualquier sistema
operativo o estructura de proyecto."
"""
