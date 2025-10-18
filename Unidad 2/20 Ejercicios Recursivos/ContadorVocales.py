# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Contador Vocales.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class ContadorVocales:
    def __init__(self, frase_inicial):
        self.frase = frase_inicial

    def obtener_frecuencia_vocalica(self):
        return self._inspeccionar_recursivamente(self.frase)

    def _inspeccionar_recursivamente(self, subcadena):
        if not subcadena:
            return 0

        if subcadena[0].lower() in 'aeiou':
            return 1 + self._inspeccionar_recursivamente(subcadena[1:])
        else:
            return self._inspeccionar_recursivamente(subcadena[1:])

# Ejemplo de uso de la clase:
procesador = ContadorVocales("Recursividad")
total_vocales = procesador.obtener_frecuencia_vocalica()
print(total_vocales)  # Imprime 5