import random

rango = random.randint(1, 50)
print(rango)
intento = 0
adivinanza = True

while adivinanza:
    numero = int(input("Ingrese un número entre el 1 y 50: "))
    intento += 1
    if rango == numero and intento < 10:
        print(f"Felicitaciones, el número secreto es: {numero}. Usted ha adivinado en su intento número {intento}")
        adivinanza = False
    elif rango != numero and intento < 10:
        restan_intentos = 10 - intento
        print(f"Este es su intento número {intento}, le quedan {restan_intentos} intentos")
        if numero > rango:
            print("El numero ingresado es mayor que el número secreto.")
        else:
            print("El numero ingresado es menor que el número secreto.")
    elif intento >= 10:
        print(f"Usted se ha quedado sin intentos, el número secreto es el {rango}")
        adivinanza = False
    else:
        print("Ha ingresado un número no válido")
else:
    print("El juego ha terminado")
