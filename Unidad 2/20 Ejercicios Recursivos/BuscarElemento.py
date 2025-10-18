# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Buscar Elemento.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class InspectorDeListas:
    def __init__(self, conjunto_de_datos):
        self.datos = conjunto_de_datos

    def verificar_existencia(self, item_buscado):
        return self._revisar_recursivamente(self.datos, item_buscado)

    def _revisar_recursivamente(self, sub_lista, item):
        if not sub_lista:
            return False
        elif sub_lista[0] == item:
            return True
        else:
            return self._revisar_recursivamente(sub_lista[1:], item)

# Ejemplo de uso de la clase:
inspector = InspectorDeListas([1, 3, 5, 7])
print(inspector.verificar_existencia(5))  # Imprime True
print(inspector.verificar_existencia(2))  # Imprime False