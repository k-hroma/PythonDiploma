print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union a | b: {union}')

interseccion = a & b
print(f'Intersección a & b {interseccion}')

diferencia = a - b
print(f'Diferencia a - b {diferencia}')

# set.union(*otros)
a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b)
print(union)

# set.intersection(*otros)
a = {1, 2, 3}
b = {2, 3, 4}
interseccion = a.intersection(b)
print(interseccion)

# set.difference(*otros)
a = {1, 2, 3}
b = {2, 3, 4}
diferencia = a.difference(b)
print(diferencia)

# set.symmetric_difference(*otro)
"""
Devuelve un nuevo conjunto con los elementos que están en uno u otro conjunto,
pero no en ambos.
"""
a = {1, 2, 3}
b = {2, 3, 4}
sim_diferencia = a.symmetric_difference(b)
print(sim_diferencia)

# set.issubset(otro)
"""
Devuelve True si el conjunto actual es un subconjunto del otro.
"""
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# set.isdisjoint(otro)
"""
Devuelve True si los dos conjuntos no tienen elementos en común.
"""
a = {1, 2, 3}
b = {4, 5}
print(a.isdisjoint(b)) 
