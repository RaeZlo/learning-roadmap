"""
Enumeraciones (Enum) en Python
"""
"""
El uso de `Enum` permite crear tipos de datos enumerados que son fáciles de leer y usar.
En este ejercicio, se exploraron dos casos: días de la semana y gestión de estados de pedidos,
mostrando la versatilidad de este enfoque en Python.
"""

from enum import Enum

# Definición de un Enum para representar los días de la semana
class Semana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Función para obtener el nombre del día según su número
def dia_semana(num: int):
    try:
        print(f"Día seleccionado: {Semana(num).name}")
    except ValueError:
        print("El número proporcionado no corresponde a ningún día de la semana.")

# Ejemplo de uso
dia_semana(5)  # Muestra "VIERNES"
dia_semana(8)  # Muestra un mensaje de error

"""
Extra
"""
# Definición del Enum para los estados de un pedido
class Status(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

# Clase que representa un pedido
class Pedidos:
    # Estado inicial predeterminado para todos los pedidos
    status = Status.PENDIENTE

    def __init__(self, id: int) -> None:
        """
        Constructor de la clase Pedidos.
        :param id: Identificador único del pedido.
        """
        self.id = id

    def enviar(self):
        """
        Cambia el estado del pedido a ENVIADO si está en estado PENDIENTE.
        """
        if self.status == Status.PENDIENTE:
            self.status = Status.ENVIADO
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o no está en estado PENDIENTE.")

    def entregar(self):
        """
        Cambia el estado del pedido a ENTREGADO si está en estado ENVIADO.
        """
        if self.status == Status.ENVIADO:
            self.status = Status.ENTREGADO
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancelar(self):
        """
        Cambia el estado del pedido a CANCELADO si no está en estado ENTREGADO.
        """
        if self.status != Status.ENTREGADO:
            self.status = Status.CANCELADO
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        """
        Muestra el estado actual del pedido con un mensaje descriptivo.
        """
        print(f"El estado del pedido {self.id} es {self.status.name}")

# Ejemplo de uso del sistema de gestión de pedidos
order_1 = Pedidos(1)  # Creación de un pedido con identificador 1
order_1.display_status()  # Estado inicial: PENDIENTE
order_1.entregar()  # No puede entregarse antes de ser enviado
order_1.enviar()  # Cambia a ENVIADO
order_1.entregar()  # Cambia a ENTREGADO
order_1.cancelar()  # No puede cancelarse ya que está ENTREGADO
