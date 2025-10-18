# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Factorial.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Factorial:

    def __init__(self, numero_inicial):
        self.numero = numero_inicial

    def ejecutar_calculo(self):
        return self._proceso_recursivo(self.numero)

    def _proceso_recursivo(self, num):
        if num == 1:
            return 1
        else:
            return num * self._proceso_recursivo(num - 1)


# Ejemplo de uso de la clase:
calculadora = Factorial(5)
resultado = calculadora.ejecutar_calculo()
print(resultado)  # Imprime 120