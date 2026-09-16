class Trabajador:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.porcentaje_retencion

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()


if __name__ == "__main__":
    # Datos dados del trabajador
    horas_trabajadas = 48
    valor_hora = 5000
    porcentaje_retencion = 0.125  # 12.5% de retención en la fuente

    trabajador = Trabajador(horas_trabajadas, valor_hora, porcentaje_retencion)

    salario_bruto = trabajador.calcular_salario_bruto()
    retencion = trabajador.calcular_retencion()
    salario_neto = trabajador.calcular_salario_neto()

    print(f"El salario bruto es: ${salario_bruto:.0f}")
    print(f"La retención en la fuente es: ${retencion:.0f}")
    print(f"El salario neto es: ${salario_neto:.0f}")
