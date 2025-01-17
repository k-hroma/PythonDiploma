mi_tupla = (1, "a", True)
mi_tupla2 = (3, "b", False)
mi_tupla3 = mi_tupla, mi_tupla2
print(mi_tupla3)
mi_tupla4 = mi_tupla + mi_tupla2
print(mi_tupla4)
print(mi_tupla4[1])
print(mi_tupla4.index("b"))
print(mi_tupla4.count("b"))


