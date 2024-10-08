# Clase Author
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # Lista para almacenar los libros del autor

    # Método para agregar un libro a la lista de libros del autor
    def add_book(self, book):
        self.books.append(book)

    # Método para obtener la lista de títulos de los libros del autor
    def get_books(self):
        return [book.title for book in self.books]

    # Representación en cadena del autor
    def __str__(self):
        return f"Autor: {self.name}"

# Clase Book
class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
        author.add_book(self)  # Asociar el libro con su autor automáticamente

    # Representación en cadena del libro
    def __str__(self):
        return f"Libro: {self.title}, Páginas: {self.pages}, Autor: {self.author.name}"

# Clase Library
class Library:
    def __init__(self):
        self.books = []  # Lista para almacenar todos los libros en la biblioteca

    # Método para agregar un libro a la biblioteca
    def add_book(self, book):
        self.books.append(book)

    # Método para listar los libros de un autor específico
    def list_books_by_author(self, author):
        libros_del_autor = [book for book in self.books if book.author == author]
        if libros_del_autor:
            print(f"Libros de {author.name}:")
            for book in libros_del_autor:
                print(f"- {book.title} ({book.pages} páginas)")
        else:
            print(f"{author.name} no tiene libros en la biblioteca.")

