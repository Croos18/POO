class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, categoria={self.categoria}, isbn={self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, id_usuario={self.id_usuario})"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = {}  # Diccionario con ID de usuario como clave

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido quitado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
            # Devolver todos los libros prestados al eliminar el usuario
            for libro in usuario.libros_prestados:
                self.libros[libro.isbn] = libro
            usuario.libros_prestados.clear()
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"No se encontró el libro con ISBN {isbn}.")
            return
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        libro = self.libros.pop(isbn)
        usuario = self.usuarios[id_usuario]
        usuario.libros_prestados.append(libro)
        print(f"Libro con ISBN {isbn} prestado al usuario con ID {id_usuario}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        usuario = self.usuarios[id_usuario]
        libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
        if libro is None:
            print(f"El libro con ISBN {isbn} no está prestado al usuario con ID {id_usuario}.")
            return

        usuario.libros_prestados.remove(libro)
        self.libros[isbn] = libro
        print(f"Libro con ISBN {isbn} devuelto por el usuario con ID {id_usuario}.")

    def buscar_libro(self, criterio, valor):
        if criterio not in ["titulo", "autor", "categoria"]:
            print(f"Criterio de búsqueda '{criterio}' no válido. Debe ser 'titulo', 'autor' o 'categoria'.")
            return []

        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            return resultados
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")
            return []

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return []

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            return usuario.libros_prestados
        else:
            print(f"El usuario con ID {id_usuario} no tiene libros prestados.")
            return []

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nOpciones:")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Selecciona una opción (1-9): ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que lo pide: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            criterio = input("Criterio de búsqueda (titulo, autor, categoria): ")
            valor = input(f"Valor para {criterio}: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            for libro in resultados:
                print(libro)

        elif opcion == "8":
            id_usuario = input("ID del usuario para listar libros prestados: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            for libro in libros_prestados:
                print(libro)

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
