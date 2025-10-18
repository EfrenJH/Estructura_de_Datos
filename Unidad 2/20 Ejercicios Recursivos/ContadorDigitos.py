# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Contador Digitos.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class ContadorDigitos:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial

    def ejecutar_conteo(self):
        return self._conteo_recursivo_interno(self.valor)

    def _conteo_recursivo_interno(self, cifra):
        if cifra < 10:
            return 1
        else:
            return 1 + self._conteo_recursivo_interno(cifra // 10)

# Ejemplo de uso de la clase:
calculadora = ContadorDigitos(12345)
cantidad = calculadora.ejecutar_conteo()
print(cantidad)  # Imprime 5