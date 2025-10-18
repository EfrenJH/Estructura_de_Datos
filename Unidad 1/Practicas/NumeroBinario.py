# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Numero Binario.py    Ejercicios
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


def binario_a_decimal(binario):
    pila = Pila()

    for digito in binario:
        if digito in '01':
            pila.push(int(digito))
        else:
            return "Error: El string contiene caracteres no binarios."

    decimal = 0
    potencia = 0

    while not pila.is_empty():
        valor = pila.pop()
        decimal += valor * (2 ** potencia)
        potencia += 1

    return decimal

binario1 = "1011"
print(f"Binario: {binario1}")
print(f"Decimal: {binario_a_decimal(binario1)}")

print("-" * 20)

binario2 = "110101"
print(f"Binario: {binario2}")
print(f"Decimal: {binario_a_decimal(binario2)}")

print("-" * 20)

binario_invalido = "1021"
print(f"Binario: {binario_invalido}")
print(f"Decimal: {binario_a_decimal(binario_invalido)}")