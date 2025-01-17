socios = ["juan", "pedro", "susana", "anna", "sofia", "pablo"]
ajedrez = ["pedro", "susana", "anna", "sofia", "pablo"]
natacion = ["juan", "pedro", "susana"]
resultado = set(ajedrez).intersection(set(natacion))
print(resultado)
print(type(resultado))
