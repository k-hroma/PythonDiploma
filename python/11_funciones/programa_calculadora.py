print("\n ***Programa Calculadora***")


def sumar(a, b):
    resultado = a + b
    print(resultado)


def restar():
    a = int(input("Ingrese valor1: "))
    b = int(input("Ingrese valor2: "))
    resultado = a - b
    print(resultado)


def multiplicar():
    pass


def dividir():
    pass


def menu():
    while True:
        print("\nMenú:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir")
        opcion = int(input("Elija que operación desea realizar: \n"))
        if opcion == 1:
            sumar(a=int(input("Ingrese valor 1: ")), b=int(input("Ingrese valor 2: ")))
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            break
        else:
            print("Su selección no es válida. Elija una operación del Menú.")


menu()