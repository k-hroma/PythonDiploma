print('*** Factorial del Número 5 ***')

# Definimos la funcion factorial recursiva
def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

numero = 5
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es: {resultado}')

"""
5xfac(4)
4xfac(3)
3xfac(2)
2xfac(1)
return 1
2x1 = 2 :fac2=2
3x2 = 6 :fac3=6
4x6 = 24:fac4=24
5x24=120:fac5=120
"""