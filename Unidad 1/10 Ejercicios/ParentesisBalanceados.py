# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Parentesis Balanceados.py    Bloque de 10 Programas
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

def parentesis_balanceados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()

    return pila.is_empty()

# Prueba
expresion_valida = "((a+b)*c)"
expresion_invalida1 = "(a+b))("
expresion_invalida2 = "((8+9)*6"

print(f"'{expresion_valida}' -> {'La expresión matemática es válida' if parentesis_balanceados(expresion_valida) else 'La expresión matemática NO es válida'}")
print(f"'{expresion_invalida1}' -> {'La expresión matemática es válida' if parentesis_balanceados(expresion_invalida1) else 'La expresión matemática NO es válida'}")
print(f"'{expresion_invalida2}' -> {'La expresión matemática es válida' if parentesis_balanceados(expresion_invalida2) else 'La expresión matemática NO es válida'}")
     