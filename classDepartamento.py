# departamento.py
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.areas = []

    def agregar_area(self, area):
        self.areas.append(area)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_areas(self):
        return self.areas
