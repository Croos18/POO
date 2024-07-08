# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        pass  # Método a ser sobrescrito en las clases derivadas


# Definición de la clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza  # Encapsulación del atributo raza

    def emitir_sonido(self):
        return "¡Guau!"  # Polimorfismo: método sobrescrito


# Definición de la clase derivada Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.__color = color  # Encapsulación del atributo color

    def emitir_sonido(self):
        return "¡Miau!"  # Polimorfismo: método sobrescrito


# Creación de instancias y demostración del programa
def main():
    # Creación de instancias
    mi_perro = Perro("Fido", 5, "Labrador")
    mi_gato = Gato("Mittens", 3, "Gris")

    # Acceso a los métodos y atributos
    print(f"{mi_perro.nombre} dice: {mi_perro.emitir_sonido()}")
    print(f"{mi_gato.nombre} dice: {mi_gato.emitir_sonido()}")


if __name__ == "__main__":
    main()