# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Suma Natural.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class SumaNatural:
    def __init__(self, numero_tope):
        self.tope = numero_tope

    def obtener_total(self):
        return self._sumar_recursivamente(self.tope)

    def _sumar_recursivamente(self, valor):
        if valor == 1:
            return 1
        else:
            return valor + self._sumar_recursivamente(valor - 1)

# Ejemplo de uso de la clase:
serie = SumaNatural(5)
total = serie.obtener_total()
print(total)  # Imprime 15