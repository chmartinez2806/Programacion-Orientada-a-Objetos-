class CalculadoraEdades:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def calcular_edad_alberto(self):
        return self.edad_juan * 2 / 3

    def calcular_edad_ana(self):
        return self.edad_juan * 4 / 3

    def calcular_edad_mama(self, edad_ana, edad_alberto):
        return self.edad_juan + edad_ana + edad_alberto


if __name__ == "__main__":
    edad_juan = float(input("Ingrese la edad de Juan: "))

    calculadora = CalculadoraEdades(edad_juan)
    edad_alberto = calculadora.calcular_edad_alberto()
    edad_ana = calculadora.calcular_edad_ana()
    edad_mama = calculadora.calcular_edad_mama(edad_ana, edad_alberto)

    print(f"La edad de Juan es: {edad_juan}")
    print(f"La edad de Alberto es: {edad_alberto}")
    print(f"La edad de Ana es: {edad_ana}")
    print(f"La edad de la mamá es: {edad_mama}")
