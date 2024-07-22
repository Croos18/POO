class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

class ClimaSemanal:
    def __init__(self):
        self.clima_diario = ClimaDiario()

    def mostrar_promedio(self):
        self.clima_diario.ingresar_temperaturas()
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    print("Programa de Promedio Semanal del Clima (Programación Orientada a Objetos)")
    clima_semanal = ClimaSemanal()
    clima_semanal.mostrar_promedio()