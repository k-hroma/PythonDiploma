# Defino las variables globales
lista_copmra = []
lista_snacks = [
    {"Id": 1, "Nombre": "Papas fritas", "Precio": 1000},
    {"Id": 2, "Nombre": "Coca Cola", "Precio": 1300},
    {"Id": 3, "Nombre": "Galletitas", "Precio": 800}
    ]
total = 0

# Defino las funciones
def elegir_snack():
    print("\n--- Snacks disponibles ---\n")
    for producto in lista_snacks:
        print(f'ID: {producto["Id"]} <--> {producto["Nombre"]} <--> ${producto.get("Precio")}')


def comprar_snack():
    global total
    global lista_copmra
    id_cliente = int(
        input("Ingrese el ID del producto que desea comprar: ")
        )
    for producto in lista_snacks:
        if id_cliente == producto["Id"]:
            print(f"Se ha agregado el producto: {producto} a su lista de compra")
            valores = producto.values()
            id, producto, precio = valores
            producto_agregado = list(valores)
    lista_copmra.append(producto_agregado)
    print("\nSu Ticket de compra al momento:")
    for producto in lista_copmra:
        print(producto)
        precio = producto[2]
        total = total + precio
    print(f' Total $ {total} pesos')


def eliminar_snack():
    global lista_copmra
    global total
    print("\nSu Ticket de compra al momento:")
    for producto in lista_copmra:
        print(producto)
    id_cliente = int(
        input("Ingrese el código del producto que desea eliminar: ")
        )
    for producto in lista_copmra:
        if producto[0] == id_cliente:
            print(f"Se ha eliminado el producto: {producto} de su lista de compra")
            lista_copmra.remove(producto)         
    print("\nSu Ticket de compra al momento:")
    for producto in lista_copmra:
        print(producto)
        precio = producto[2]
        total = total - precio
    print(f'El total de su compra es $ {total} pesos')


def mostrar_ticket():
    global total
    global lista_copmra
    print("\nTicket de compra:")

    for producto in lista_copmra:
        print(producto)
        precio = producto[2]
        total = total + precio
    print(f'El total de su compra es $ {total} pesos')

# Defino el ciclo infinito hasta que se de la condición para la salida
while True:
    print("\n--- Menu disponible ---\n1.Elegir snack\n2.Comprar snack\n3.Eliminar snack\n4.Mostrar ticket\n5.Salir\n")

    opcion = int(input("Ingrese una opción disponible: "))
    if opcion == 1:
        elegir_snack()
    elif opcion == 2:
        comprar_snack()
    elif opcion == 3:
        eliminar_snack()
    elif opcion == 4:
        mostrar_ticket()
    elif opcion == 5:
        print("Usted ha salido del sistema.")
        break
    else:               
        print("Esa opción no es valida")
