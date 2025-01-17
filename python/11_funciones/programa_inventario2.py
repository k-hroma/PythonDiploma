print("""*** Sistema de Inventarios ***""")

lista_producto = []


def buscar_producto():
    id_buscar = int(input("Ingrese el ID que desea buscar: "))
    for producto in lista_producto:
        if producto[0] == id_buscar:  # El ID está en la posición 0 de cada lista
            print(f"Producto encontrado: ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
            return
    print("No existe un producto con el ID ingresado.")


def salir():
    print("Usted ha salido del sistema de inventario.")


def ver_inventario():
    print(lista_producto)


def agregar_producto():
    global lista_producto
    print("Ingrese los datos del producto: ")
    id = int(input("ID: "))
    if id in lista_producto:
        print("El id ingresado ya existe")
        return
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    nvo_producto = [id, nombre, precio, cantidad]
    lista_producto.append(nvo_producto)
    print(lista_producto)


def menu():
    while True:
        opcion = int(input("\n\t___Menú___\n\n\t 1.Mostrar inventario\n\t 2.Agregar nuevo producto\n\t 3.Buscar producto por ID\n\t 4.Salir\n\nElija una opción: "))
        if opcion == 1:
            ver_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            salir()
            break
        else:
            print("Opción no válida. Intente nuevamente.")


menu()
