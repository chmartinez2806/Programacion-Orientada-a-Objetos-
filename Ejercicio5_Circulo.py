import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_longitud(self):
        return 2 * math.pi * self.radio


if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))

    mi_circulo = Circulo(radio)

    print(f"El área del círculo es: {mi_circulo.calcular_area()}")
    print(f"La longitud de la circunferencia es: {mi_circulo.calcular_longitud()}")
