print("""*** Sistema de Inventarios ***""")

diccionario_producto = {}


def buscar_producto_nombre():
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ").lower()
    encontrado = False
    for id_producto, datos_producto in diccionario_producto.items():
        if datos_producto["Nombre"].lower() == nombre_buscar:
            print(f"ID: {id_producto}, Datos: {datos_producto}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")


def buscar_producto_id():
    id_buscar = int(input("Ingrese el id que desea buscar: "))
    if id_buscar in diccionario_producto:
        print(diccionario_producto[id_buscar])


def salir():
    print("Usted ha salido del sistema de inventario.")


def ver_inventario():
    print(diccionario_producto)


def agregar_producto():
    global diccionario_producto
    print("Ingrese los datos del producto: ")
    id = int(input("ID: "))
    if id in diccionario_producto:
        print("El id ingresado ya existe")
        return
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    diccionario_producto[id] = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    print(diccionario_producto)


def menu():
    while True:
        opcion = int(input("\n\t___Menú___\n\n\t 1.Mostrar inventario\n\t 2.Agregar nuevo producto\n\t 3.Buscar producto por ID\n\t 4.Salir\n\t 5.Buscar producto por nombre\n\nElija una opción: "))
        if opcion == 1:
            ver_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_id()
        elif opcion == 4:
            salir()
        elif opcion == 5:
            buscar_producto_nombre()
        else:
            print("Opción no válida. Intente nuevamente.")
            break


menu()
