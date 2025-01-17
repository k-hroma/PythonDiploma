entero1 = 3
entero2 = 21
lista1 = [True, "pera", 4]
# print(entero1, entero2, lista1)
# print(entero1, entero2, lista1, sep=" / ", end="!\t")
# print(entero1, entero2, lista1)

print(lista1)
a, b, c = [True, "pera", 4]
print(a, b, c)

a, *b = [True, "pera", 4]
print(a, b, type(b))

a, *b = "Pera"
print(a, b, type(b))
