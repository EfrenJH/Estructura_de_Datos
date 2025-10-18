# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Conversión de Decimal A Binario.py    Bloque de 10 Programas
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

    def is_empty(self):
        return len(self.items) == 0

def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"

    pila = Pila()

    while numero_decimal > 0:
        residuo = numero_decimal % 2
        pila.push(residuo)
        numero_decimal = numero_decimal // 2

    binario = ""
    while not pila.is_empty():
        binario += str(pila.pop())

    return binario

try:
    print("* * * Conversión de Decimal a Binario * * *")
    num = int(input("\nIngresa un número decimal para convertir a binario: "))
    resultado_binario = decimal_a_binario(num)
    print(f"✅ El resultado es: {resultado_binario}")
except ValueError:
    print("❌ Error: Por favor, ingresa un número entero válido.")