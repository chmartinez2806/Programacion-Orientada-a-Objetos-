class Potenciacion:
    def calcular_cuadrado(self, numero):
        return numero ** 2

    def calcular_cubo(self, numero):
        return numero ** 3


if __name__ == "__main__":
    numero = float(input("Numero: "))

    potencia = Potenciacion()
    cuadrado = potencia.calcular_cuadrado(numero)
    cubo = potencia.calcular_cubo(numero)

    print(f"El cuadrado de {round(numero)} es: {round(cuadrado)}")
    print(f"El cubo de {round(numero)} es: {round(cubo)}")
