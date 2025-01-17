productos = [
    {"Id": 1, "Nombre": "papas", "Precio": 1000},
    {"Id": 2, "Nombre": "coca", "Precio": 900},
    {"Id": 3, "Nombre": "arroz", "Precio": 700}
    ]

lista_productos = []


def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    if productos:
        for producto in productos:
            print(f"\tId: {producto.get('Id')} -> {producto.get('Nombre')} -> ${producto.get('Precio')}")


def buscar_snack_por_id(id_buscar):
    for producto in productos:
        if producto.get("Id") == id_buscar:
            return producto
    return None


def mostrar_ticket():
    print("\n***Ticket de compra cliente***\n")
    total = 0
    for i, producto in enumerate(lista_productos, start=1):
        print(f"Producto {i}. {producto.get('Nombre')}: $ {producto.get('Precio')}")
        total += producto.get("Precio")
    print(f"\nTotal de la compra: {total}")


def comprar_snacks():
    id_producto = int(input('Qué snack quieres comprar (id): '))
    snack_encontrado = buscar_snack_por_id(id_producto)
    if snack_encontrado is not None:
        lista_productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_producto}')


def menu():
    while True:  #con while True hacemos que el ciclo se repita infinitamente // se rompe en break
        print("\n\n***Maquina de snacks***\n\nMENÚ:\n\t 1.Mostrar Snacks\n\t 2.Comprar Snacks\n\t 3.Mostrar Snacks\n\t 4.Salir\n")

        opcion = int(input("Escoja una opción: "))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Gracias por su compra.4")
            break
        else:
            print("La opcion ingresada es incorrecta.")


menu()