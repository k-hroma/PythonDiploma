def contador_yield(max):
    n = 0
    print("1--------------------------1")
    while n < max:
        yield n
        print("2--------------------------2")
        n += 1


d = contador_yield(3)
print(d)
print("Ejecución de inicio de yield")
print(next(d))
print("Ejecución de yield")
print(next(d))
print("Ejecución de yield")
print(next(d))
