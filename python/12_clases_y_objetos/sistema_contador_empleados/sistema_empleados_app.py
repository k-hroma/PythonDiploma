from empresa import Empresa
from empleados import Empleados
print("*** Sistema de Empleados***")

# crear una instancia de la clase Empresa
empresa1 = Empresa("Porche")

# contratar empleados = crear objetos de tipo Empleados
empresa1.contratar_empleados("Rocio", "Marketing")
empresa1.contratar_empleados("María", "Marketing")
empresa1.contratar_empleados("Juana", "Ventas")
empresa1.contratar_empleados("Sofía", "Recursos humanos")

# obtener el total de objetos de tipo empleado
print(f"Total de empleados: {Empleados.obtener_total_empleados()}")

# obtener el número de empleados en el departamento de ventas
print(f"{empresa1.obtener_numero_empleados_por_departamento('Marketing')}")

# mostrar todos los empleados de la Empresa1
empresa1.obtener_total_empleados()