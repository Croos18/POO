# Definición de la clase Vuelo
class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero.nombre} {pasajero.apellido} añadido al vuelo {self.numero}")
        else:
            print(f"¡El vuelo {self.numero} está completo!")

# Definición de la clase Pasajero
class Pasajero:
    def __init__(self, nombre, apellido, numero_pasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_pasaporte = numero_pasaporte

# Definición de la clase Reserva
class Reserva:
    def __init__(self, vuelo, pasajero):
        self.vuelo = vuelo
        self.pasajero = pasajero

    def confirmar_reserva(self):
        self.vuelo.agregar_pasajero(self.pasajero)
        # Creación de instancias de vuelos
vuelo1 = Vuelo("BA123", "LHR", "JFK", 250)
vuelo2 = Vuelo("AF456", "CDG", "SFO", 200)

# Creación de instancias de pasajeros
pasajero1 = Pasajero("Juan", "Pérez", "ABC123")
pasajero2 = Pasajero("María", "Gómez", "DEF456")

# Creación de reservas
reserva1 = Reserva(vuelo1, pasajero1)
reserva2 = Reserva(vuelo2, pasajero2)

# Confirmación de reservas
reserva1.confirmar_reserva()  # Esto añadirá pasajero1 al vuelo1
reserva2.confirmar_reserva()  # Esto añadirá pasajero2 al vuelo2