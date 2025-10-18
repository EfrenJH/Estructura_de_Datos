# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Mayuscula Primera Letra.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

"""
En Mayúsculas -> DETERMINÍSTICO
Crea una función que reciba un String de cualquier tipo y se encargue de:
- Poner en mayúscula la primera letra de cada palabra
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente

Determinar qué operaciones:
Es de tipo BINARIO (dado que se van a realizar comparaciones por cada uno de los carácteres)

Determinar conjuntos de datos:
Espacios en blanco y que si la primera letra ya se encuentra en mayúscula

Análisis a priori:
Se compara cada carácter de la longitud de todo el String

Análisis a posteriori:
Conforme va avanzando las comparaciones del String el tiempo va a ir aumentando
"""
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def front(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def mayuscula(texto):
    if not texto:
        return ""

    cola = Cola()
    for caracter in texto:
        cola.enqueue(caracter)

    resultado = ""
    inicio_de_palabra = True

    while not cola.is_empty():
        caracter = cola.dequeue()
        if inicio_de_palabra and 'a' <= caracter <= 'z':
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
        inicio_de_palabra = (caracter == " ")

    return resultado


texto = "hola mundo esto es una prueba"
print("Texto original:", texto)
print("Texto convertido:", mayuscula(texto))

texto2 = "  otra   prueba con   espacios "
print("\nTexto original:", texto2)
print("Texto convertido:", mayuscula(texto2))