from cliente import Cliente
from sucursal import Sucursal
from nodo_servicio import NodoServicio

class SistemaBanco:
    def __init__(self):
        self.clientes_cola = []  # Cola de atención
        self.clientes_prioritarios = []  # Lista de clientes prioritarios
        self.historial_pila = []  # Pila para el historial de atenciones
        self.sucursales = []  # Lista de sucursales
        self.servicios = NodoServicio("Servicios")  # Árbol de servicios
        self.grafo_sucursales = {}  # Grafo de sucursales
        self.diccionario_clientes = {}  # Diccionario de clientes

    # Método para agregar cliente a la cola
    def agregar_cliente(self, cliente):
        if cliente.es_prioritario:
            self.clientes_prioritarios.append(cliente)  # Agregar a lista de prioritarios
            print(f"Cliente prioritario {cliente.nombre} agregado a la lista de atención.")
        else:
            self.clientes_cola.append(cliente)  # Agregar a la cola regular
            print(f"Cliente {cliente.nombre} agregado a la cola de espera.")

        self.diccionario_clientes[cliente.id_cliente] = cliente

    # Método para atender cliente
    def atender_cliente(self):
        if self.clientes_prioritarios:
            cliente = self.clientes_prioritarios.pop()  # Atender el último prioritario
        elif self.clientes_cola:
            cliente = self.clientes_cola.pop(0)  # Atender el primero de la cola
        else:
            print("No hay clientes en espera.")
            return None
        
        self.historial_pila.append(cliente)
        print(f"Cliente {cliente.nombre} atendido.")
        return cliente

    # Método para agregar sucursal
    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)
        self.grafo_sucursales[sucursal] = sucursal.conexiones

    # Método para agregar servicio en el árbol
    def agregar_servicio(self, categoria, subservicio):
        for servicio in self.servicios.subservicios:
            if servicio.nombre == categoria:
                servicio.agregar_subservicio(NodoServicio(subservicio))
                print(f"Subservicio '{subservicio}' agregado a la categoría '{categoria}'")
                return
        nueva_categoria = NodoServicio(categoria)
        nueva_categoria.agregar_subservicio(NodoServicio(subservicio))
        self.servicios.agregar_subservicio(nueva_categoria)
        print(f"Categoría '{categoria}' y subservicio '{subservicio}' agregados al árbol de servicios.")

    # Método para conectar dos sucursales en el grafo
    def conectar_sucursales(self, sucursal1, sucursal2, distancia):
        sucursal1.agregar_conexion(sucursal2, distancia)
        sucursal2.agregar_conexion(sucursal1, distancia)
        print(f"Sucursales '{sucursal1.nombre}' y '{sucursal2.nombre}' conectadas con distancia {distancia}.")

    # Método para consultar el historial de un cliente usando el diccionario
    def consultar_historial_cliente(self, id_cliente):
        cliente = self.diccionario_clientes.get(id_cliente)
        if cliente:
            print(f"Historial del cliente {cliente.nombre}: {cliente.historial_atencion}")
            return cliente.historial_atencion
        else:
            print("Cliente no encontrado.")
            return None

    # Método para atender y registrar historial de clientes con selección de servicio
    def atender_y_registrar_historial(self):
        while self.clientes_prioritarios or self.clientes_cola:
            cliente_atendido = self.atender_cliente()
            if cliente_atendido:
                # Mostrar servicios disponibles y pedir selección
                print("Servicios disponibles:")
                for servicio in self.servicios.subservicios:
                    print(f"- {servicio.nombre}: {[sub.nombre for sub in servicio.subservicios]}")
                
                servicio_seleccionado = input(f"Seleccione un servicio para el cliente {cliente_atendido.nombre}: ")
                servicio_encontrado = False
                
                for servicio in self.servicios.subservicios:
                    for subservicio in servicio.subservicios:
                        if subservicio.nombre == servicio_seleccionado:
                            cliente_atendido.agregar_historial(servicio_seleccionado)
                            servicio_encontrado = True
                            break
                if not servicio_encontrado:
                    print(f"Servicio '{servicio_seleccionado}' no encontrado. No se registrará en el historial.")