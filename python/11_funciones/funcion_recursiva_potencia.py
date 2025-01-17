# Calcular la potencia de un número usando una función recursiva
# n a la b = n*n a la (b-1) = (n° = n*n*n (°=3))  
# n = 2
# ° = 3
# = 2(3) = 2*2*2 = 8

# caso base, exponente == 0 --------> 1


def recursiva_potencia(base, exponente):
    if exponente == 0:
        print(f"{base} elevada a la 0 es = 1")
        return 1
    else:
        return base * recursiva_potencia(base, exponente - 1)


resultado = recursiva_potencia(5, 5)
print(f"El resultado es = {resultado}")
