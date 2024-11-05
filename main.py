
from cliente import Cliente
from sucursal import Sucursal
from nodo_servicio import NodoServicio
from sistema_banco import SistemaBanco

def main():
    # Crear sistema de banco
    sistema = SistemaBanco()

    # Crear clientes
    cliente1 = Cliente(1, "Juan")
    cliente2 = Cliente(2, "Ana", es_prioritario=True)
    cliente3 = Cliente(3, "Luis")
    cliente4 = Cliente(4, "María", es_prioritario=True)

    # Agregar clientes al sistema
    sistema.agregar_cliente(cliente1)
    sistema.agregar_cliente(cliente2)
    sistema.agregar_cliente(cliente3)
    sistema.agregar_cliente(cliente4)

    # Crear sucursales
    sucursal1 = Sucursal("Sucursal Centro")
    sucursal2 = Sucursal("Sucursal Norte")
    sucursal3 = Sucursal("Sucursal Sur")

    # Agregar sucursales al sistema
    sistema.agregar_sucursal(sucursal1)
    sistema.agregar_sucursal(sucursal2)
    sistema.agregar_sucursal(sucursal3)

    # Conectar sucursales (grafo)
    sistema.conectar_sucursales(sucursal1, sucursal2, 10)  # Conectar Centro - Norte
    sistema.conectar_sucursales(sucursal1, sucursal3, 15)  # Conectar Centro - Sur
    sistema.conectar_sucursales(sucursal2, sucursal3, 20)  # Conectar Norte - Sur

    # Agregar servicios al árbol de servicios
    sistema.agregar_servicio("Cuentas", "Apertura de cuenta")
    sistema.agregar_servicio("Cuentas", "Cierre de cuenta")
    sistema.agregar_servicio("Préstamos", "Solicitud de préstamo")
    sistema.agregar_servicio("Préstamos", "Revisión de estado de préstamo")

    # Atender clientes y registrar su historial
    sistema.atender_y_registrar_historial()

    # Consultar historial de cliente
    sistema.consultar_historial_cliente(2)  # Consulta historial del cliente Ana

if __name__ == "__main__":
    main()