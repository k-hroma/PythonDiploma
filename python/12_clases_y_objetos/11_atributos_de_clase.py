class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa principal
if __name__ == '__main__':
    print(f'*** Atributos de Clase ***')
    print(f'Atributo de Clase: {Persona.atributo_clase}')
    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de Clase: {Persona.atributo_clase}')

    # Creamos un objeto persona1
    persona1 = Persona(15)
    print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}')  # no es la mejor práctica, para acceder a un atributo de clase es recomendable hacerlo desde la clase.
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}')
    persona2.atributo_clase = 20
    print(persona2.atributo_clase) # solo modifiqué el atributo de clase para el objeto "persona2"
    print(persona1.atributo_clase)
    print(Persona.atributo_clase)
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')
