"""
Test Unitarios en Python
"""
"""
   - Test Unitario:
     - Es una técnica de testing utilizada para comprobar que las funciones individuales de un programa funcionan según lo esperado.
     - Se enfoca en la validación de pequeñas unidades de código de manera aislada.
   - unittest:
     - Es un framework incorporado en Python para realizar pruebas unitarias.
     - Proporciona herramientas para definir, ejecutar y verificar tests.
"""

import unittest
from datetime import datetime, date

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b

# Clase de Pruebas Unitarias para la función `sum`
class TestSum(unittest.TestCase):

    # Test: Verifica que la función `sum` retorna resultados correctos.
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    # Test: Verifica que la función `sum` lanza un error con tipos de datos incorrectos.
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)

"""
Extra
"""
class TestData(unittest.TestCase):

    def setUp(self):
        # Configuración inicial antes del test.
        self.datos = {
            "name": "Rafael", 
            "age": 19, 
            "birth_date": datetime.strptime("22-01-05", "%d-%m-%y").date(), 
            "programming_languages": ["Python", "Java"]
        }

    # Test: Verifica que el diccionario contiene todas las claves necesarias.
    def test_campos_existentes(self):
        self.assertIn("name", self.datos)
        self.assertIn("age", self.datos)
        self.assertIn("birth_date", self.datos)
        self.assertIn("programming_languages", self.datos)

    # Test: Verifica que los tipos de los valores en el diccionario sean correctos.
    def test_tipo_datos(self):
        self.assertIsInstance(self.datos["name"], str)
        self.assertIsInstance(self.datos["age"], int)
        self.assertIsInstance(self.datos["birth_date"], date)
        self.assertIsInstance(self.datos["programming_languages"], list)

"""
Ejecución de las Pruebas
"""
if __name__ == "__main__":
    unittest.main()
