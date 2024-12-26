"""
Clases en Python
"""

"""
Concepto de Clases:
- Una clase es una plantilla que define las propiedades y el comportamiento de un conjunto de objetos.
- Permite estructurar el código en bloques reutilizables y organizados.
- Cada clase puede contener:
  * Atributos: Propiedades que describen el estado de un objeto.
  * Métodos: Funciones que definen el comportamiento de un objeto.
  * Constructor (__init__): Método especial que se ejecuta al crear una instancia (objeto) de la clase.
"""

class Gato:

    # Atributo de clase (común para todos los objetos)
    raza: str = None

    # Constructor: Define atributos específicos de cada objeto
    def __init__(self, color: str, nombre: str, edad: int, sonido: str):
        self.color = color  
        self.nombre = nombre  
        self.edad = edad  
        self.sonido = sonido  

    # Método: Imprime la información del gato
    def imprimir(self):
        print(f"Nombre: {self.nombre} | Color: {self.color} | Edad: {self.edad} | Sonido: {self.sonido} | Raza: {self.raza}")

# Crear una instancia de la clase `Gato`
gato = Gato("Naranja", "Afri", 13, "Miau")
gato.imprimir()

# Modificar un atributo
gato.raza = "Callejero"
gato.imprimir()
print("")  # Separador visual

"""
Extra
"""
class Stack:

    # Constructor: Inicializa la pila como una lista vacía
    def __init__(self):
        self.stack = []

    # Método: Añadir un elemento a la pila (push)
    def push(self, item):
        self.stack.append(item)

    # Método: Eliminar y devolver el último elemento de la pila (pop)
    def pop(self):
        if self.size() == 0:  # Verifica si la pila está vacía
            return None
        return self.stack.pop()

    # Método: Retornar el número de elementos en la pila
    def size(self):
        return len(self.stack)

    # Método: Imprimir el contenido de la pila
    def imprimir(self):
        for item in reversed(self.stack):  # Muestra los elementos desde el último hasta el primero
            print(item)

# Crear una instancia de la clase `Stack`
stack = Stack()
stack.push("Pedro")
stack.push(18)
stack.imprimir()
print("Elemento eliminado:", stack.pop())
print("Número de elementos:", stack.size())
print("")  # Separador visual

class Queue:

    # Constructor: Inicializa la cola como una lista vacía
    def __init__(self):
        self.queue = []

    # Método: Añadir un elemento a la cola (enqueue)
    def enqueue(self, item):
        self.queue.append(item)

    # Método: Eliminar y devolver el primer elemento de la cola (dequeue)
    def dequeue(self):
        if self.size() == 0:  # Verifica si la cola está vacía
            return None
        return self.queue.pop(0)

    # Método: Retornar el número de elementos en la cola
    def size(self):
        return len(self.queue)

    # Método: Imprimir el contenido de la cola
    def imprimir(self):
        for item in self.queue:  # Muestra los elementos desde el primero hasta el último
            print(item)

# Crear una instancia de la clase `Queue`
queue = Queue()
queue.enqueue("Ron")
queue.enqueue(20)
queue.enqueue(13.78654)
queue.imprimir()
print("Elemento eliminado:", queue.dequeue())
print("Número de elementos:", queue.size())
