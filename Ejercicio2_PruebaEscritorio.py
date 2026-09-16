class PruebaEscritorio:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def calcular(self):
        self.suma += self.x
        self.x = self.x + self.y ** 2
        self.suma = self.suma + (self.x / self.y)
        return self.suma


if __name__ == "__main__":
    prueba = PruebaEscritorio()
    resultado = prueba.calcular()
    print(f"EL VALOR DE LA SUMA ES: {resultado}")
