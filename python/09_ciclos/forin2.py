mi_diccionario = {}
mi_diccionario2 = {}
mi_diccionario3 = {}
cantidad_elementos = 5

for e in range(0, cantidad_elementos):
    a = str(e + 1)
    print(f'{"Ingrese un numero"}==>{a}')
    b = int(input())

    if b % 2 == 0:
        print("El valor es par")
        cond = "es par"
    else:
        print("El valor no es par")
        cond = "es impar"

    mi_dic = {b: cond}

    print(mi_dic)
    mi_diccionario[e] = b
    mi_diccionario2[e] = cond
    mi_diccionario3[e] = "El número " + str(b) + "es: " + cond

print(mi_diccionario)
print(mi_diccionario2)
print(mi_diccionario3)

print("---" * 23)

for x in mi_diccionario3:
    print(mi_diccionario3[x])
