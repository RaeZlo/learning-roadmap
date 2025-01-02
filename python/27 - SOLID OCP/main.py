"""
Principio SOLID: Abierto-Cerrado (Open-Close Principle, OCP)
------------------------------------------------------------
El Principio Abierto-Cerrado establece que las entidades de software (clases, módulos, funciones) deben estar 
abiertas para su extensión, pero cerradas para su modificación.

Esto significa que podemos añadir nuevas funcionalidades a nuestro sistema sin modificar el código existente, 
lo que reduce el riesgo de introducir errores y facilita la mantenibilidad.

Ejemplo: Implementación Correcta e Incorrecta del OCP
"""

# Incorrecto: Sistema que viola el OCP al requerir modificar el código existente para agregar nuevas funcionalidades.
class Calculator:
    def calculate(self, operation, a, b):
        if operation == "addition":
            return a + b
        elif operation == "subtraction":
            return a - b
        elif operation == "multiplication":
            return a * b
        elif operation == "division":
            return a / b
        else:
            raise ValueError("Operación no soportada")

# Correcto: Sistema que cumple con el OCP al permitir agregar nuevas operaciones sin modificar el código existente.
from abc import ABC, abstractmethod

class Operation(ABC):
    """
    Clase base abstracta para definir operaciones matemáticas.
    """
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("División por cero no permitida")
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Calculator:
    """
    Calculadora que permite realizar operaciones matemáticas cumpliendo con el OCP.
    """
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation):
        """
        Agrega una nueva operación a la calculadora.
        """
        self.operations[name] = operation

    def calculate(self, name, a, b):
        """
        Realiza el cálculo utilizando la operación especificada.
        """
        if name not in self.operations:
            raise ValueError(f"La operación '{name}' no está soportada.")
        return self.operations[name].execute(a, b)

# Prueba del sistema de calculadora
calculator = Calculator()

# Agregar operaciones básicas
calculator.add_operation("addition", Addition())
calculator.add_operation("subtraction", Subtraction())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())

# Probar las operaciones básicas
print("Resultados de las operaciones básicas:")
print(f"Suma: {calculator.calculate('addition', 10, 5)}")
print(f"Resta: {calculator.calculate('subtraction', 10, 5)}")
print(f"Multiplicación: {calculator.calculate('multiplication', 10, 5)}")
print(f"División: {calculator.calculate('division', 10, 5)}")

# Agregar una nueva operación (potencia) sin modificar el código existente
calculator.add_operation("power", Power())

# Probar la nueva operación
print("\nResultado de la nueva operación (potencia):")
print(f"Potencia: {calculator.calculate('power', 10, 3)}")
