# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Decimal A Binario.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class DecimalABinario:
    def __init__(self, numero_base_diez):
        self.numero_decimal = numero_base_diez

    def a_binario(self):
        if self.numero_decimal == 0:
            return "0"
        return self._proceso_recursivo_conversion(self.numero_decimal)

    def _proceso_recursivo_conversion(self, numero):
        if numero == 0:
            return ''
        else:
            return self._proceso_recursivo_conversion(numero // 2) + str(numero % 2)

# Ejemplo de uso de la clase:
convertidor = DecimalABinario(10)
representacion_binaria = convertidor.a_binario()
print(representacion_binaria)  # Imprime "1010"