print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAXIMO = 5
numero = 0
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'\nResultado suma acumulada: {acumulador_suma}')

"""
*** Suma Acumulativa ***
(acumulador_suma + numero) -> 0 + 0
Suma parcial acumulada: 0

(acumulador_suma + numero) -> 0 + 1
Suma parcial acumulada: 1

(acumulador_suma + numero) -> 1 + 2
Suma parcial acumulada: 3

(acumulador_suma + numero) -> 3 + 3
Suma parcial acumulada: 6

(acumulador_suma + numero) -> 6 + 4
Suma parcial acumulada: 10

(acumulador_suma + numero) -> 10 + 5
Suma parcial acumulada: 15


Resultado suma acumulada: 15
"""
