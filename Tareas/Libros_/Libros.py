# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.disponible = True  # Estado inicial: disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True  # Préstamo exitoso
        else:
            return False  # El libro ya está prestado

    def devolver(self):
        self.disponible = True

    def info_libro(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}, Disponible: {self.disponible}"

# Definición de la clase Socio
class Socio:
    def __init__(self, nombre, apellido, num_socio):
        self.nombre = nombre
        self.apellido = apellido
        self.num_socio = num_socio
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True  # Préstamo exitoso
        else:
            return False  # El libro no está disponible

    def devolver_libro(self, libro):
        libro.devolver()
        self.libros_prestados.remove(libro)

    def info_socio(self):
        return f"Socio {self.num_socio}: {self.nombre} {self.apellido}, Libros prestados: {len(self.libros_prestados)}"

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.socios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def eliminar_socio(self, socio):
        self.socios.remove(socio)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None  # Si no se encuentra el libro

    def buscar_libro_por_autor(self, autor):
        libros_autor = []
        for libro in self.libros:
            if libro.autor == autor:
                libros_autor.append(libro)
        return libros_autor

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Creación de algunos libros
    libro1 = Libro("El Hobbit", "J.R.R. Tolkien", 300)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 400)

    # Creación de algunos socios
    socio1 = Socio("Juan", "Pérez", 1001)
    socio2 = Socio("María", "Gómez", 1002)

    # Creación de la biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Añadir libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Añadir socios a la biblioteca
    biblioteca.agregar_socio(socio1)
    biblioteca.agregar_socio(socio2)

    # Préstamo de libros
    socio1.prestar_libro(libro1)
    socio2.prestar_libro(libro2)

    # Información
    print(libro1.info_libro())
    print(libro2.info_libro())
    print(socio1.info_socio())
    print(socio2.info_socio())