"""
Principio SOLID: Responsabilidad Única (Single Responsibility Principle, SRP)
------------------------------------------------------------------------------
El Principio de Responsabilidad Única establece que una clase debe tener una 
única razón para cambiar, es decir, debe estar enfocada en una sola responsabilidad.

Ventajas:
1. Mejora la mantenibilidad del código, ya que cada clase tiene una responsabilidad clara.
2. Facilita la reutilización del código en diferentes contextos.
3. Reduce el acoplamiento entre componentes, permitiendo un diseño más modular y flexible.

Ejemplo: Implementación Correcta e Incorrecta del SRP
"""

# Incorrecto: Una clase que viola el SRP al manejar múltiples responsabilidades
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def save_to_database(self):
        # Lógica para guardar el usuario en la base de datos
        pass

    def send_email(self):
        # Lógica para enviar un correo electrónico
        pass

# Correcto: Separar las responsabilidades en diferentes clases
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserService:
    def save_to_database(self, user):
        # Lógica para guardar el usuario en la base de datos
        pass

class EmailService:
    def send_email(self, email, message):
        # Lógica para enviar un correo electrónico
        pass

print("-" * 50)

"""
Dificultad Extra:
-----------------
Desarrollar un sistema de gestión para una biblioteca siguiendo el SRP. 
Incluye funcionalidades para registrar libros, usuarios y procesar préstamos.
"""

# Incorrecto: Una clase que maneja múltiples responsabilidades, violando el SRP
class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append({"user_id": user_id, "book_title": book_title})
                return True
        return False

    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                    return True
        return False

# Correcto: Separar las responsabilidades en diferentes clases
class Book:
    """
    Clase que representa un libro en el sistema de biblioteca.
    """
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class User:
    """
    Clase que representa un usuario en el sistema de biblioteca.
    """
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

class Loan:
    """
    Clase que gestiona los préstamos de libros.
    """
    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"user_id": user.id, "book_title": book.title})
            return True
        return False

    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False

class Library:
    """
    Clase principal que coordina las operaciones de libros, usuarios y préstamos.
    """
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loan_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loan_service.loan_book(user, book)
        return False

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loan_service.return_book(user, book)
        return False

# Ejemplo de uso del sistema de biblioteca
library = Library()

# Crear libros y usuarios
book1 = Book("Clean Code", "Robert C. Martin", 3)
book2 = Book("The Pragmatic Programmer", "Andy Hunt", 2)
user1 = User("Alice", 1, "alice@example.com")
user2 = User("Bob", 2, "bob@example.com")

# Registrar libros y usuarios
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

# Realizar préstamos
library.loan_book(1, "Clean Code")
library.loan_book(2, "The Pragmatic Programmer")

# Devolver libros
library.return_book(1, "Clean Code")
