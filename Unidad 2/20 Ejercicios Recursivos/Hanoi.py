# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Hanoi.py    20 Programas Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Hanoi:
    def __init__(self, cantidad_discos, poste_origen="A", poste_destino="C", poste_auxiliar="B"):
        self.discos = cantidad_discos
        self.origen = poste_origen
        self.destino = poste_destino
        self.auxiliar = poste_auxiliar

    def iniciar_solucion(self):
        self._resolver_recursivamente(self.discos, self.origen, self.destino, self.auxiliar)

    def _resolver_recursivamente(self, n, salida, llegada, apoyo):
        if n == 1:
            print(f"Mover disco desde {salida} hacia {llegada}")
        else:
            self._resolver_recursivamente(n - 1, salida, apoyo, llegada)
            self._resolver_recursivamente(1, salida, llegada, apoyo)
            self._resolver_recursivamente(n - 1, apoyo, llegada, salida)

# Ejemplo de uso de la clase:
hanoi = Hanoi(3)
hanoi.iniciar_solucion()