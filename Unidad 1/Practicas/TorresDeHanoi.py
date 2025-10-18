# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Torres De Hanoi.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

contador_movimientos = 0

def hanoi(n, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar):
    global contador_movimientos

    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        contador_movimientos += 1
        print(f"({contador_movimientos}) Mover disco {disco} de Torre {nombre_origen} a Torre {nombre_destino}")
        return

    hanoi(n - 1, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino)

    disco = origen.pop()
    destino.push(disco)
    contador_movimientos += 1
    print(f"({contador_movimientos}) Mover disco {disco} de Torre {nombre_origen} a Torre {nombre_destino}")

    hanoi(n - 1, auxiliar, destino, origen, nombre_auxiliar, nombre_destino, nombre_origen)



torre_A = Pila()
torre_B = Pila()
torre_C = Pila()

try:
    num_discos = int(input("Ingrese la cantidad de discos para la Torre de Hanoi: "))
    if num_discos <= 0:
        print("Por favor, ingrese un número positivo de discos.")
    else:
        for i in range(num_discos, 0, -1):
            torre_A.push(i)

        print("\n--- ESTADO INICIAL ---")
        print(f"Torre A: {torre_A}")
        print(f"Torre B: {torre_B}")
        print(f"Torre C: {torre_C}")
        print("\n--- COMIENZAN LOS MOVIMIENTOS ---")

        hanoi(num_discos, torre_A, torre_B, torre_C, 'A', 'B', 'C')

        print("\n--- ESTADO FINAL --- 🏁")
        print(f"Torre A: {torre_A}")
        print(f"Torre B: {torre_B}")
        print(f"Torre C: {torre_C}")
        print(f"\n Se completó en un total de {contador_movimientos} movimientos.")

except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero.")