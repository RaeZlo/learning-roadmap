"""
Principio SOLID: Sustitución de Liskov (Liskov Substitution Principle, LSP)
---------------------------------------------------------------------------
El Principio de Sustitución de Liskov establece que los objetos de una clase derivada deben poder ser reemplazados
por objetos de su clase base sin alterar el funcionamiento del programa. 

Esto garantiza que el comportamiento de un sistema se mantenga consistente al trabajar con una jerarquía de clases.

Ejemplo: Implementación Correcta e Incorrecta del LSP
"""

# Incorrecto: Sistema que viola el LSP al no mantener el comportamiento esperado en una clase derivada.
class Bird:
    def fly(self):
        return "Flying"

class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollos no vuelan")

# Esto rompe el LSP porque `Chicken` no se comporta como un `Bird`.
# bird = Bird()
# print(bird.fly())  # "Flying"
# chicken = Chicken()
# print(chicken.fly())  # Exception: "Los pollos no vuelan"

# Correcto: Diseño que cumple con el LSP al mantener la consistencia en la jerarquía.
class Bird:
    def move(self):
        return "Moving"

class Chicken(Bird):
    def move(self):
        return "Walking"

# Probando el cumplimiento del LSP
bird = Bird()
print(bird.move())  # "Moving"

chicken = Chicken()
print(chicken.move())  # "Walking"

# Cambiar instancias sigue siendo consistente
bird = Chicken()
print(bird.move())  # "Walking"

chicken = Bird()
print(chicken.move())  # "Moving"

"""
DIFICULTAD EXTRA: Jerarquía de Vehículos cumpliendo el LSP
----------------------------------------------------------
Crear un sistema de vehículos que permita acelerar y frenar, asegurando que todas las clases derivadas
mantienen el comportamiento consistente con la clase base.
"""

class Vehicle:
    """
    Clase base para todos los vehículos.
    """
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        """
        Incrementa la velocidad del vehículo.
        """
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        """
        Reduce la velocidad del vehículo.
        """
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")

class Car(Vehicle):
    """
    Clase derivada que representa un coche.
    """
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)

class Bicycle(Vehicle):
    """
    Clase derivada que representa una bicicleta.
    """
    def accelerate(self, increment):
        print("La bicicleta está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta está frenando")
        super().brake(decrement)

class Motorcycle(Vehicle):
    """
    Clase derivada que representa una motocicleta.
    """
    def accelerate(self, increment):
        print("La moto está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La moto está frenando")
        super().brake(decrement)

def test_vehicle(vehicle):
    """
    Función de prueba que verifica el comportamiento de los vehículos.
    """
    vehicle.accelerate(10)
    vehicle.brake(5)

# Creando instancias de vehículos
car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

print("\nProbando el coche:")
test_vehicle(car)

print("\nProbando la bicicleta:")
test_vehicle(bicycle)

print("\nProbando la motocicleta:")
test_vehicle(motorcycle)

"""
Características del sistema
---------------------------
1. Diseño modular: Todas las subclases heredan de la clase base `Vehicle`.
2. Cumplimiento del LSP: Cada subclase (Car, Bicycle, Motorcycle) puede sustituir a `Vehicle` sin afectar el sistema.
3. Extensibilidad: Es sencillo agregar nuevos vehículos que implementen las mismas operaciones (`accelerate` y `brake`).
"""
