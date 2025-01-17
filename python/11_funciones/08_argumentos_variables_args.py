print('*** Argumentos Variables ***')


def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')

    # Crear una lista para almacenar los superpoderes
    superpoderes = []
    # Iteramos los superpoderes y agregarlos a una lista
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
        superpoderes.append(superpoder)
    return superpoderes  # opcional

# Llamar la funcion y se obtiene la lista


lista_superpoderes = superheroe_superpoderes(
    'Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
lista2_superpoderes = superheroe_superpoderes(
    'Ironam', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

# Es opcional enviar argumentos variables
lista3_superpoderes = superheroe_superpoderes('Mi vecino', 'Juan Perez')
lista_final = [lista_superpoderes, lista2_superpoderes, lista3_superpoderes]
print(lista_final)


def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')

    # Crear una lista para almacenar los superpoderes
    superpoderes = ()
    # Iteramos los superpoderes y agregarlos a una lista
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
        superpoderes += (superpoder,)
    return superpoderes  # opcional

# Llamar la funcion y se obtiene la tupla


lista_superpoderes = superheroe_superpoderes(
    'Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
lista2_superpoderes = superheroe_superpoderes(
    'Ironam', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

# Es opcional enviar argumentos variables
lista3_superpoderes = superheroe_superpoderes('Mi vecino', 'Juan Perez')
lista_final = [lista_superpoderes, lista2_superpoderes, lista3_superpoderes]
print(lista_final)