# director.py
from classEmpleado import Empleado

class Director(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, puesto="Director")
