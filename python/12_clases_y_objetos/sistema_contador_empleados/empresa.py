from empleados import Empleados


class Empresa():

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    # defino el método de instancia que almacena los datos de una lista
    def contratar_empleados(self, nombre, departamento):
        # creo una instancia de la clase Empleados e inicializo los valores a través de su constructor
        empleado = Empleados(nombre, departamento)
        # agrego el objeto empleado a la lista vacía
        self.empleados.append(empleado)

    # defino el método de instancia que contará los empleados por departamento
    def obtener_numero_empleados_por_departamento(self, departamento):
        # inicio el contador en 0
        contador_empleados_por_departamento = 0
        # recorro la lista de empleados
        for empleado in self.empleados:
            # si el valor del departamento dentro de la lista coincide con el valor del departamento que está recibiendo el método, entonces se suma 1 al contador
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1
        # devuelve el número total de empleados encontrados en la lista.
        return contador_empleados_por_departamento

    def obtener_total_empleados(self, ):
        print(f"\nTotal de empleados para la empresa {self.nombre}")
        for empleado in self.empleados:
            print(f"""Empleado {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}""")
