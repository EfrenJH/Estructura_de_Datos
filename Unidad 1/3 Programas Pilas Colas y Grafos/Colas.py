#Instrituto Tecnológico de San Juan del Río
#Ingeniería en Sistemas Computacionales
#Estructura de Datos
#Unidad 1
#Colas.py    3 Programas: Pilas, Colas y Grafos
#Docente: Domingo Rosales Alvarez
#Efrén Jacobo Hernández
#No. de control: 24590384

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


# Simulación
cola_banco = Cola()
cola_banco.enqueue("Ana")
cola_banco.enqueue("Luis")
cola_banco.enqueue("María")

print("Atendiendo:", cola_banco.dequeue())  # Ana
print("Atendiendo:", cola_banco.dequeue())  # Luis
print("Atendiendo:", cola_banco.dequeue())  # María