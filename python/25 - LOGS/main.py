"""
Logging en Python
-----------------------------------
El módulo `logging` es una herramienta fundamental para capturar eventos de un programa, como errores,
información de estado o eventos críticos.

Características Principales:
1. Permite capturar mensajes en diferentes niveles de severidad:
   - DEBUG: Información detallada, útil para diagnosticar problemas.
   - INFO: Confirmación de que las cosas están funcionando como se espera.
   - WARNING: Una indicación de que algo inesperado sucedió, pero el programa continúa funcionando.
   - ERROR: Un problema más serio que impide que el programa realice una función específica.
   - CRITICAL: Un error grave que puede impedir que el programa continúe ejecutándose.
2. Soporte para múltiples salidas: consola, archivos, etc.
3. Configuración flexible mediante `basicConfig` o manejadores personalizados.

Ejemplo Inicial:
Configura `logging` y muestra un mensaje en cada nivel de severidad.
"""

# Configuración de logging
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de severidad que se registrará
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del mensaje
    handlers=[logging.StreamHandler()]  # Salida en la consola
)

# Ejemplo de mensajes en diferentes niveles
logging.debug("Esto es un mensaje de DEBUG.")
logging.info("Esto es un mensaje de INFO.")
logging.warning("Esto es un mensaje de WARNING.")
logging.error("Esto es un mensaje de ERROR.")
logging.critical("Esto es un mensaje de CRITICAL.")

print("-" * 50)

"""
Dificultad Extra:
-----------------
Implementación de un sistema ficticio de gestión de tareas utilizando `logging`.

Requisitos:
1. Añadir tareas: Recibe un nombre y una descripción.
2. Eliminar tareas: Identificadas por nombre.
3. Listar tareas: Imprime todas las tareas almacenadas.
4. Implementar logs:
   - INFO: Confirmaciones de acciones exitosas.
   - WARNING: Advertencias sobre intentos de acciones redundantes.
   - ERROR: Errores al realizar operaciones no válidas.
   - DEBUG: Tiempo de ejecución de cada operación y estado de la lista de tareas.
"""

class TaskManager:
    """
    Clase para gestionar tareas. Permite añadir, eliminar y listar tareas, 
    registrando eventos con diferentes niveles de logging.
    """
    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str):
        """
        Añade una tarea nueva al sistema.
        Si la tarea ya existe, genera una advertencia.
        """
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}.")
        else:
            logging.warning(f"Se ha intentado añadir una tarea que ya existe: {name}.")
        logging.debug(f"Número de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        """
        Elimina una tarea del sistema.
        Si la tarea no existe, genera un error.
        """
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea: {name}.")
        else:
            logging.error(f"Se ha intentado eliminar una tarea que no existe: {name}.")
        logging.debug(f"Número de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        """
        Lista todas las tareas almacenadas.
        Si no hay tareas, informa al usuario.
        """
        start_time = time.time()
        if self.tasks:
            logging.info(f"Se va a imprimir la lista de tareas.")
            for name, description in self.tasks.items():
                print(f"{name} - {description}")
        else:
            logging.info("No hay tareas para mostrar.")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        """
        Imprime el tiempo de ejecución de una operación.
        """
        logging.debug(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")

# Ejemplo de uso del sistema de gestión de tareas
task_manager = TaskManager()

# Listar tareas vacías
task_manager.list_tasks()

# Añadir tareas
task_manager.add_task("Pan", "Comprar 5 barras de pan.")
task_manager.add_task("Python", "Estudiar Python.")

# Listar tareas después de añadir
task_manager.list_tasks()

# Eliminar tarea existente
task_manager.delete_task("Python")

# Listar tareas después de eliminar
task_manager.list_tasks()

# Intentar añadir una tarea duplicada
task_manager.add_task("Pan", "Comprar 5 barras de pan.")

# Intentar eliminar una tarea inexistente
task_manager.delete_task("Python")
