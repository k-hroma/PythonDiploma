print('*** break y continue ***')

# Ejemplo con break
print('Palabra break:')
for numero in range(1, 10):
    if numero % 2 == 0:  # numero par
        print(numero)
        break  # Salimos del ciclo inmediatamente
        # Se imprime unicamente el primer número par

# Ejemplo con continue
print('\nPalabra continue: ')
for numero in range(1, 10):
    if numero % 2 == 1:  # numero impar (!== 0)
        continue    
        # continue con la siguiente iteración: no ejecuta la siguiente línea de código.
    print(numero)  # imprime los numeros pares
