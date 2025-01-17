"""VARIABLES Y COMENTARIOS"""
# Declaracion e inicialización de variables
edad = 28
altura = 1.65
pais = "Argentina"

# Acceder a las variables
print("Valores iniciales: ")
print("Edad:", edad)
print("Altura:", altura)
print("País:", pais)

edad = 30
altura = 1.78
pais = "Argentina"

# Modificar los valores
# se crea un nuevo objeto y la variable edad ahora apunta a ese nuevo objeto
# la direccion de memoria se pierde
print("Valores modificados: ")
print("Edad:", edad)
print("Altura:", altura)
print("País:", pais)

# En python el tipo es dinámico
edad = "treinta"
print("Valores con tipos modificados: ")
print("Edad:", edad, "de int a str")
print("Altura:", altura)
print("País:", pais)
