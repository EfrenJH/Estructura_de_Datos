# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Consonantes y Vocales.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        """Agrega un elemento a la cima de la pila."""
        self.items.append(dato)

    def pop(self):
        """Elimina y devuelve el elemento de la cima de la pila."""
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0


def separar_recursivo(cadena, i, pila_vocales, pila_consonantes):
    """Función recursiva que separa vocales y consonantes en pilas."""
    if i == len(cadena):
        return

    caracter = cadena[i].lower()

    if caracter in "aeiouáéíóú":
        pila_vocales.push(cadena[i])
    elif caracter.isalpha():
        pila_consonantes.push(cadena[i])

    separar_recursivo(cadena, i + 1, pila_vocales, pila_consonantes)


texto = input("Ingrese una cadena de texto: ")

pila_vocales = Pila()
pila_consonantes = Pila()

separar_recursivo(texto, 0, pila_vocales, pila_consonantes)

print("Pila de vocales:", pila_vocales.items)
print("Pila de consonantes:", pila_consonantes.items)
