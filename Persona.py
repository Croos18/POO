class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Args:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado una nueva persona llamada {self.nombre}.')

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se ejecuta cuando el objeto es eliminado.
        """
        print(f'{self.nombre} ha sido eliminado.')


# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan", 30)
    persona2 = Persona("María", 25)

    # Simulando la eliminación de un objeto
    del persona1
    # persona1 ha sido eliminado automáticamente debido a la eliminación explícita arriba

    # El objeto persona2 será eliminado al salir de este bloque if debido al alcance de la variable

# Salida esperada:
# Se ha creado una nueva persona llamada Juan.
# Se ha creado una nueva persona llamada María.
# Juan ha sido eliminado.
# María ha sido eliminado.