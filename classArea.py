# area.py
class Area:
    def __init__(self, nombre):
        self.nombre = nombre
        self.director = None
        self.gerente = None
        self.jefe_area = None

    def asignar_director(self, director):
        self.director = director

    def asignar_gerente(self, gerente):
        self.gerente = gerente

    def asignar_jefe_area(self, jefe_area):
        self.jefe_area = jefe_area

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_director(self):
        return self.director

    def get_gerente(self):
        return self.gerente

    def get_jefe_area(self):
        return self.jefe_area
