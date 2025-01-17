x = "Curso"

while x:
    print(x)
    x = x[1:]

print("---" * 23)

a = 1
b = 7

while a < b:
    print(a)
    a += 1  # a = a + 1

print("---" * 23)

lista = [1, 2, 3, 4]

while lista:
    c, *lista = lista
    print(c, lista)
