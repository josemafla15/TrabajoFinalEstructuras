class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = {}

    def agregar_conexion(self, otra_sucursal, distancia):
        self.conexiones[otra_sucursal] = distancia
        