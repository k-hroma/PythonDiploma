
menu = True
saldo_inicial = 1000

print("***Aplicación de cajero automático***")

while menu:
    print(
        "Operaciones que puedes realizar: \n 1. Consultar saldo\n 2. Retirar \n 3. Depositar\n 4. Salir")
    opcion = int(input("Escoje una opción: "))
    if opcion == 1:
        print(f"Su saldo actual es ${saldo_inicial}\n")
    elif opcion == 2:
        retiro = int(input("Ingrese monto a retirar: "))
        if retiro > saldo_inicial:
            print(f"Usted intentó retirar ${retiro}, su saldo actual es ${saldo_inicial}.\nNo posee saldo suficiente.\n")
        elif retiro <= saldo_inicial:
            saldo_actual = saldo_inicial - retiro
            print(f"Usted ha retirado ${retiro} y su saldo actual es: ${saldo_actual}\n")
    elif opcion == 3:
        deposito = int(input("Ingrese monto a depositar: "))
        saldo_actual = saldo_inicial + deposito
        print(f"Usted ha ingresado ${deposito} y su saldo actual es: ${saldo_actual}\n")
    elif opcion == 4:
        print("Uste ha salido del sistema.\n")
        menu = False
    else:
        print("Usted ha ingresado una opción no valida.\n")
else:
    print("Aplicación de cajero finalizada\n")