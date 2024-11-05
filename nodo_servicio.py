class NodoServicio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subservicios = []

    def agregar_subservicio(self, subservicio):
        self.subservicios.append(subservicio)