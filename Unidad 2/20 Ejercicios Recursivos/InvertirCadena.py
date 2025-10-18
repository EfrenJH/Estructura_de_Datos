# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Invertir Cadena.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class InvertirCadena:
    def __init__(self, secuencia_inicial):
        self.secuencia = secuencia_inicial

    def ejecutar_inversion(self):
        return self._invertir_recursivamente(self.secuencia)

    def _invertir_recursivamente(self, subcadena):
        if len(subcadena) == 0:
            return subcadena
        else:
            return subcadena[-1] + self._invertir_recursivamente(subcadena[:-1])

# Ejemplo de uso de la clase:
transformador = InvertirCadena("hola")
texto_invertido = transformador.ejecutar_inversion()
print(texto_invertido)  # Imprime "aloh"