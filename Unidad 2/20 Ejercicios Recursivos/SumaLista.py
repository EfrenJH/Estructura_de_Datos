# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Suma Lista.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class AcumuladorDeListas:
    def __init__(self, conjunto_numeros):
        self.numeros = conjunto_numeros

    def obtener_suma_total(self):
        return self._sumar_recursivamente(self.numeros)

    def _sumar_recursivamente(self, sub_lista):
        if not sub_lista:
            return 0
        else:
            return sub_lista[0] + self._sumar_recursivamente(sub_lista[1:])

# Ejemplo de uso de la clase:
acumulador = AcumuladorDeListas([1, 2, 3, 4, 5])
suma_final = acumulador.obtener_suma_total()
print(suma_final)  # Imprime 15