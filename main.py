# main.py
from classDepartamento import Departamento
from classArea import Area
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

def main():
    # Creación de un departamento y un área
    departamento = Departamento("Tecnología")
    area_desarollo = Area("Desarrollo de Software")
    departamento.agregar_area(area_desarollo)

    # Creación de empleados y asignación de roles
    director = Director("Ana López", 45)
    gerente = Gerente("Carlos Méndez", 40)
    jefe_area = JefeArea("Laura Ruiz", 38)

    # Asignación de roles al área
    area_desarollo.asignar_director(director)
    area_desarollo.asignar_gerente(gerente)
    area_desarollo.asignar_jefe_area(jefe_area)

    # Impresión de la estructura de organización
    print(f"Departamento: {departamento.get_nombre()}")
    for area in departamento.get_areas():
        print(f"  Área: {area.get_nombre()}")
        print(f"    Director: {area.get_director().get_nombre()}")
        print(f"    Gerente: {area.get_gerente().get_nombre()}")
        print(f"    Jefe de Área: {area.get_jefe_area().get_nombre()}")

if __name__ == "__main__":
    main()
