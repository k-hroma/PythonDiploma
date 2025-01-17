# break
# continue

a = 1
b = 7

while a < b:
    print(a)
    a += 1  # a = a + 1

    if a > 5:
        break
    if a > 2:
        continue

    print("---: ", a)
"""
a
1    1     2
2    2
3    3
4    4
5    5

"""
