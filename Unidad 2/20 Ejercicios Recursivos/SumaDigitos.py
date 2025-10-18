# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Suma Digitos.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class SumaDigitos:
    def __init__(self, cifra_completa):
        self.numero_completo = cifra_completa

    def obtener_total(self):
        return self._acumular_recursivamente(self.numero_completo)

    def _acumular_recursivamente(self, remanente):
        if remanente == 0:
            return 0
        else:
            return remanente % 10 + self._acumular_recursivamente(remanente // 10)

# Ejemplo de uso de la clase:
agregador = SumaDigitos(1234)
total_digitos = agregador.obtener_total()
print(total_digitos)  # Imprime 10