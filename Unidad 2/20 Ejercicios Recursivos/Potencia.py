# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Potencia.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class OperacionExponencial:
    def __init__(self, numero_base, numero_exponente):
        self.base = numero_base
        self.exponente = numero_exponente

    def obtener_resultado(self):
        return self._multiplicar_recursivamente(self.base, self.exponente)

    def _multiplicar_recursivamente(self, base_val, exp_val):
        if exp_val == 0:
            return 1
        else:
            return base_val * self._multiplicar_recursivamente(base_val, exp_val - 1)

# Ejemplo de uso de la clase:
operacion = OperacionExponencial(2, 3)
resultado_final = operacion.obtener_resultado()
print(resultado_final)  # Imprime 8