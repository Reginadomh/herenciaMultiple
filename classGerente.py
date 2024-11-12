# gerente.py
from classEmpleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, puesto="Gerente")
