"""
Principio SOLID: Segregación de Interfaces (Interface Segregation Principle, ISP)
--------------------------------------------------------------------------------
El Principio de Segregación de Interfaces establece que una clase no debe estar obligada 
a implementar interfaces que no utiliza. En lugar de tener una interfaz grande con muchos métodos, 
debemos dividirla en interfaces más pequeñas y específicas.

Esto mejora la flexibilidad y la mantenibilidad del código al evitar que clases implementen métodos innecesarios.

Ejemplo: Implementación Incorrecta y Correcta del ISP
"""

# Sin ISP: La interfaz `WorkerInterface` obliga a las clases a implementar métodos innecesarios
# en función de su tipo, como es el caso de la clase `Robot` que no necesita el método `eat`.
class WorkerInterface(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(WorkerInterface):
    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkerInterface):
    def work(self):
        print("Trabajando")

    def eat(self):
        # Los robots no comen, pero deben implementar `eat` debido a la interfaz `WorkerInterface`.
        pass


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()  # El robot no necesita comer, pero debe implementar el método `eat` de la interfaz


# Con ISP: Se crean interfaces más pequeñas y específicas para que las clases sólo implementen los métodos que necesitan
class WorkInterface(ABC):
    @abstractmethod
    def work(self):
        pass


class EatInterface(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(WorkInterface, EatInterface):
    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkInterface):
    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

"""
DIFICULTAD EXTRA: Gestor de Impresoras aplicando ISP
---------------------------------------------------
En este ejercicio, se crea un sistema de impresoras en el que se implementan diferentes tipos de impresoras.
Algunas sólo imprimen en blanco y negro, otras sólo imprimen a color y otras son multifuncionales.

El sistema aplica el Principio de Segregación de Interfaces para que las clases de impresoras solo implementen 
las interfaces necesarias para su funcionalidad.

Requisitos:
1. Las impresoras básicas solo deben poder imprimir (en blanco y negro).
2. Las impresoras a color deben poder imprimir a color.
3. Las impresoras multifuncionales deben poder imprimir, escanear y enviar fax.

Implementación del sistema y verificación del cumplimiento del ISP.
"""

class PrinterInterface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass


class ColorPrinterInterface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass


class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document: str) -> str:
        pass


class FaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass


# Impresora básica: solo imprime en blanco y negro
class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")


# Impresora a color: solo puede imprimir a color
class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")


# Impresora multifuncional: puede imprimir, escanear y enviar fax
class MultifunctionPrinter(PrinterInterface, ColorPrinterInterface, ScannerInterface, FaxInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")

    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")

    def scan(self, document: str) -> str:
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."

    def send_fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")


def test_printers():
    """
    Función de prueba para verificar el funcionamiento de las impresoras.
    """
    printer = Printer()
    color_printer = ColorPrinter()
    multifunction_printer = MultifunctionPrinter()

    # Imprimir en blanco y negro
    printer.print("doc.pdf")

    # Imprimir a color
    color_printer.print_color("doc.pdf")

    # Imprimir, escanear y enviar fax con impresora multifuncional
    multifunction_printer.print("doc.pdf")
    multifunction_printer.print_color("doc.pdf")
    multifunction_printer.scan("doc.pdf")
    multifunction_printer.send_fax("doc.pdf")


test_printers()

"""
Características del sistema
---------------------------
1. Las impresoras implementan solo las interfaces necesarias según su funcionalidad.
2. Cumplimiento del ISP: Las impresoras no están obligadas a implementar métodos innecesarios (por ejemplo, una impresora 
   básica no tiene que implementar `print_color`, y una impresora a color no tiene que implementar `scan` o `send_fax`).
3. Extensibilidad: Se pueden agregar nuevas impresoras con funciones adicionales sin modificar las clases existentes.
"""
