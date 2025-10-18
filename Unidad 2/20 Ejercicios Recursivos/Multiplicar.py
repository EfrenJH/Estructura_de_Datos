# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Multiplicar.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Multiplicar:
    def __init__(self, factor1, factor2):
        self.factor_a = factor1
        self.factor_b = factor2

    def obtener_producto(self):
        return self._sumar_recursivamente(self.factor_a, self.factor_b)

    def _sumar_recursivamente(self, numero, contador):
        if contador == 0:
            return 0
        else:
            return numero + self._sumar_recursivamente(numero, contador - 1)

# Ejemplo de uso de la clase:
calculo = Multiplicar(3, 4)
producto_final = calculo.obtener_producto()
print(producto_final)  # Imprime 12