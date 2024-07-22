import math

def calcular_area_radio(radio):
    return math.pi * radio ** 2

def main():
    radio = 5
    area = calcular_area_radio(radio)
    if area > 100:
        print(f"El área del círculo con radio {radio} es mayor que 100.")
    else:
        print(f"El área del círculo con radio {radio} es menor o igual que 100.")

if __name__ == "__main__":
    main()
