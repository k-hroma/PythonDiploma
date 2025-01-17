# la variable_2 apunta al objeto que apunta la variable_1, no a la variable_1 directamente

variable_1 = "pera"
variable_2 = variable_1
print(variable_1, variable_2)

variable_1 = "auto"
print(variable_1, variable_2)
