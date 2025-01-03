"""
Principio SOLID: Inversión de Dependencias (Dependency Inversion Principle, DIP)
--------------------------------------------------------------------------------
El Principio de Inversión de Dependencias establece que las clases de alto nivel no deben depender de clases de bajo nivel,
sino de abstracciones. Las abstracciones no deben depender de los detalles, sino los detalles deben depender de las abstracciones.

Este principio tiene como objetivo mejorar la flexibilidad y la mantenibilidad del sistema, permitiendo que las clases de alto nivel
no se vean afectadas por cambios en las clases de bajo nivel.

Ejemplo: Implementación Incorrecta y Correcta del DIP
"""

# Sin DIP: La clase `Lamp` depende directamente de la clase `Switch`, lo que hace que cualquier cambio en `Switch` 
# afecte directamente a `Lamp`.
class Switch:

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self) -> None:
        self.switch = Switch()  # Lamp depende directamente de Switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp()
lamp.operate("on")
lamp.operate("off")


# Con DIP: Se crea una interfaz abstracta `AbstractSwitch` que es implementada por `LampSwitch`. 
# Esto permite que `Lamp` no dependa directamente de la implementación de `Switch`, sino de una abstracción.
class AbstractSwitch:

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LampSwitch(AbstractSwitch):

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")


class Lamp:

    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch  # Lamp depende de la abstracción AbstractSwitch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp(LampSwitch())  # Lamp recibe la implementación de switch
lamp.operate("on")
lamp.operate("off")


"""
DIFICULTAD EXTRA: Sistema de Notificaciones aplicando DIP
--------------------------------------------------------
En este ejercicio, se crea un sistema de notificaciones que puede enviar diferentes tipos de mensajes (Email, PUSH, SMS).
El sistema de notificaciones no debe depender directamente de las implementaciones específicas, sino de una abstracción.

Requisitos:
1. El sistema puede enviar mensajes por Email, PUSH y SMS.
2. El sistema de notificaciones no puede depender de las implementaciones específicas.
3. Se debe usar el DIP para que las clases de alto nivel (como `NotificationService`) dependan de las abstracciones.

Implementación del sistema de notificaciones utilizando DIP.
"""

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando email con texto: {message}")


class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando PUSH con texto: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS con texto: {message}")


class NotificationService:

    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier  # El servicio de notificación depende de la abstracción `Notifier`

    def notify(self, message: str):
        self.notifier.send(message)  # Se llama al método send de la implementación de `Notifier`


# Test de notificaciones: El servicio de notificación puede recibir cualquier implementación de `Notifier`
# Dependiendo del tipo de notificador, el mensaje será enviado de manera diferente

# Prueba con EmailNotifier
service = NotificationService(EmailNotifier())
service.notify("¡Hola, notificador por email!")

# Prueba con PUSHNotifier
service = NotificationService(PUSHNotifier())
service.notify("¡Hola, notificador por PUSH!")

# Prueba con SMSNotifier
service = NotificationService(SMSNotifier())
service.notify("¡Hola, notificador por SMS!")

"""
Características del sistema:
---------------------------
1. `NotificationService` depende de la abstracción `Notifier`, lo que permite que pueda funcionar con diferentes 
   tipos de notificadores sin necesidad de modificar la clase `NotificationService`.
2. Se cumple el DIP ya que las clases de alto nivel (`NotificationService`) no dependen de detalles de bajo nivel 
   (como `EmailNotifier`, `PUSHNotifier`, o `SMSNotifier`), sino de la abstracción `Notifier`.
3. El sistema es extensible: si se desea agregar un nuevo tipo de notificación, simplemente se implementa una nueva clase 
   que herede de `Notifier` y se pasa al `NotificationService` sin necesidad de modificar el código existente.
"""
