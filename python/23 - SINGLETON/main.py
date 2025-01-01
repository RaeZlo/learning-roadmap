"""
Patrón de Diseño Singleton
--------------------------
El patrón Singleton asegura que una clase tenga una única instancia global en toda la aplicación. 
Es útil en escenarios donde se necesita garantizar que solo exista una instancia de un objeto, como en 
el manejo de configuraciones o sesiones.

Características del Singleton:
1. Restringe la creación de múltiples instancias.
2. Ofrece un punto de acceso global a la instancia única.
"""

class Singleton:
    """
    Ejemplo Genérico de Singleton
    -----------------------------
    Esta clase restringe la creación de múltiples instancias asegurándose
    de que siempre se retorne la misma instancia.
    """
    _instance = None

    def __new__(cls):
        # Verifica si ya existe una instancia; si no, la crea.
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Comprobación del patrón Singleton
singleton1 = Singleton()
print("Instancia 1 del Singleton:", singleton1)

singleton2 = Singleton()
print("Instancia 2 del Singleton:", singleton2)

# Verifica si ambas referencias apuntan al mismo objeto
print("¿Ambas referencias son la misma instancia?", singleton1 is singleton2)

print("-" * 50)

"""
Dificultad Extra
----------------
Implementación del patrón Singleton para una clase de sesión de usuario.
La clase `UserSession` gestiona la información de un usuario activo en una aplicación.
"""

class UserSession:
    """
    Clase Singleton para gestionar la sesión de usuario.
    """
    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        # Garantiza que solo exista una instancia
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, id: int, username: str, name: str, email: str):
        """
        Establece los datos del usuario en la sesión.
        """
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        """
        Recupera los datos del usuario de la sesión en formato de texto.
        """
        if self.id is None:
            return "No hay usuario en la sesión."
        return f"ID: {self.id}, Username: {self.username}, Nombre: {self.name}, Email: {self.email}"

    def clear_user(self):
        """
        Borra los datos del usuario de la sesión.
        """
        self.id = None
        self.username = None
        self.name = None
        self.email = None

# Ejemplo de uso de UserSession
print("Gestión de la sesión de usuario:")
session1 = UserSession()
print(session1.get_user())  # No hay usuario en la sesión

# Estableciendo un usuario
session1.set_user(1, "mouredev", "Brais Moure", "mouredev@gmail.com")
print("Usuario asignado a la sesión 1:", session1.get_user())

# Verificando que todas las referencias usan la misma instancia
session2 = UserSession()
print("Datos desde la sesión 2:", session2.get_user())

# Limpiando la sesión desde otra referencia
session3 = UserSession()
session3.clear_user()
print("Datos después de limpiar la sesión desde sesión 3:", session3.get_user())

"""
Conclusión:
-----------
El patrón Singleton es ideal para casos como la gestión de sesiones, donde es necesario
asegurar que solo exista una instancia compartida para manejar datos globales.
"""
