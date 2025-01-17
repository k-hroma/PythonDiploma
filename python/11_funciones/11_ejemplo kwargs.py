print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():   # se aplica el unpacking
        print(f'{llave}:{valor}')
    

imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')



# Llamamos a la funcion


print("operacion suma")

suma_edades = 0


def imprimir_detalle_persona(**kwargs):
    global suma_edades
    for clave, valor in kwargs.items():
        print(clave, valor)
    if kwargs["edad"]:
        suma_edades += kwargs["edad"]


imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')

print(suma_edades)