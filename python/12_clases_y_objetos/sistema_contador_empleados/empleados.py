# creo la clase empleado
class Empleados():

    # creo un atributo de clase
    contador_empleados = 0

    # defino el constructor de la clase y sus parámetros
    # es un método de instancia
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.id = Empleados.contador_empleados + 1
        # aumento en uno por cada objeto empleado que se crea en la clase Empresa
        Empleados.contador_empleados += 1

    # defino el método de clase que devuelve el total de empleados
    @classmethod
    def obtener_total_empleados(cls, ):
        return cls.contador_empleados
