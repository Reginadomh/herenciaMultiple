# jefe_area.py
from classEmpleado import Empleado

class JefeArea(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, puesto="Jefe de Área")
