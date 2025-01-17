print('*** Alcance de Variables ***')

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # incrementamos la variable global
    contador_global += 1
    # incrementar la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias vece la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')


y = 20  # Alcance global

def otra_funcion():
    print(y)  # Se puede acceder a la variable global

otra_funcion()  # 20
print(y, "desde afuera de la f(x)")


def funcion_externa():
    a = 5  # Variable en alcance "enclosing"

    def funcion_interna():
        nonlocal a  # Si no estuviese esta variabla daría error
        a += 1  # Modifica 'a' en el alcance de la función externa
        print(a)

    funcion_interna()
    print(a)


funcion_externa()
# 6
# 6

