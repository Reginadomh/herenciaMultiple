# empleado.py
from classPersona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def get_puesto(self):
        return self.puesto

    def set_puesto(self, puesto):
        self.puesto = puesto
