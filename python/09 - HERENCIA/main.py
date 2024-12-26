"""
Herencia y Polimorfismo en Python
"""
"""
Conceptos Clave:

1. Herencia:
   - La herencia permite que una clase (subclase) herede los atributos y métodos de otra clase (superclase).
   - Facilita la reutilización de código y la organización jerárquica de clases.

2. Polimorfismo:
   - Es la capacidad de usar un mismo método en diferentes clases, pero con comportamientos específicos según la clase.
   - Esto se logra redefiniendo métodos en las subclases (sobrescritura).
"""
class Animal:  # Superclase
    def __init__(self, name: str):
        self.name = name

    # Método genérico que puede ser sobrescrito en las subclases
    def sound(self):
        pass


class Perro(Animal):  # Subclase
    def sound(self):
        print(f"{self.name} dice: Guau")


class Gato(Animal):  # Subclase
    def sound(self):
        print(f"{self.name} dice: Miau")

# Función que utiliza polimorfismo
def print_sound(animal: Animal):
    animal.sound()

# Creación de instancias y uso de la función polimórfica
perro = Perro("Walter")
print_sound(perro)

gato = Gato("Escobar")
print_sound(gato)
print("")  # Separador visual

"""
Dificultad Extra
"""
"""
Jerarquía de una empresa:
- Una superclase `Empleado` almacena los atributos y funciones comunes a todos los empleados.
- Subclases especializadas (`Manager`, `ProjectManager`, `Programmer`) definen comportamientos únicos.
"""
class Empleado:  # Superclase
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.subordinados = []

    # Método para asignar empleados al cargo
    def asignar_empleado(self, empleado):
        self.subordinados.append(empleado)

    # Método para imprimir empleados a cargo
    def imprimir_empleados(self):
        if not self.subordinados:
            print(f"{self.name} no tiene empleados a cargo.")
        else:
            print(f"Empleados a cargo de {self.name}:")
            for empleado in self.subordinados:
                print(f" - {empleado.name}")


class Manager(Empleado):  # Subclase
    def coordinar_proyectos(self):
        print(f"{self.name} está coordinando los proyectos.")


class ProjectManager(Empleado):  # Subclase
    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id, name)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f"{self.name} está coordinando el proyecto {self.proyecto}.")


class Programmer(Empleado):  # Subclase
    def __init__(self, id: int, name: str, lenguaje: str):
        super().__init__(id, name)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.name} está programando en {self.lenguaje}.")

    # Los programadores no asignan empleados
    def asignar_empleado(self, empleado):
        print(f"{self.name} no puede asignar empleados.")


# Creación de instancias
manager = Manager(1, "MoureDev")
pm1 = ProjectManager(2, "Brais", "Proyecto 1")
pm2 = ProjectManager(3, "Moure", "Proyecto 2")

dev1 = Programmer(4, "Kontrol", "Swift")
dev2 = Programmer(5, "Ros", "Cobol")
dev3 = Programmer(6, "Bushi", "Java")
dev4 = Programmer(7, "Nasos", "Python")

# Asignar subordinados
manager.asignar_empleado(pm1)
manager.asignar_empleado(pm2)

pm1.asignar_empleado(dev1)
pm1.asignar_empleado(dev2)

pm2.asignar_empleado(dev3)
pm2.asignar_empleado(dev4)

# Mostrar jerarquía y acciones
manager.coordinar_proyectos()
manager.imprimir_empleados()

pm1.coordinar_proyecto()
pm1.imprimir_empleados()

dev1.programar()
dev1.imprimir_empleados()  # No tiene subordinados
