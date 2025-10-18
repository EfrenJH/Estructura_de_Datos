# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Permutaciones.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Permutaciones:
    def __init__(self, coleccion_original):
        self.coleccion = coleccion_original

    def mostrar_permutaciones(self):
        self._construir_permutacion(self.coleccion, 0)

    def _construir_permutacion(self, sub_lista, indice_actual):
        if indice_actual == len(sub_lista) - 1:
            print(sub_lista)
        else:
            for i in range(indice_actual, len(sub_lista)):
                sub_lista[indice_actual], sub_lista[i] = sub_lista[i], sub_lista[indice_actual]
                
                self._construir_permutacion(sub_lista, indice_actual + 1)
                
                sub_lista[indice_actual], sub_lista[i] = sub_lista[i], sub_lista[indice_actual]

# Ejemplo de uso de la clase:
organizador = Permutaciones([1, 2, 3])
organizador.mostrar_permutaciones()