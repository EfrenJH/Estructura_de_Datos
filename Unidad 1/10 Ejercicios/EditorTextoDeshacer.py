# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Editor de Texto Deshacer.py    Bloque de 10 Programas
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

historial = Pila()
texto_actual = ""

while True:
    print("-" * 30)
    print(f"Texto actual: '{texto_actual}'")
    print("\nOpciones:")
    print("1. Escribir (agrega texto al final)")
    print("2. Deshacer (vuelve al estado anterior)")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        historial.push(texto_actual)

        texto_a_agregar = input("Escribe el texto a agregar: ")
        texto_actual += texto_a_agregar
        texto_actual += " "
        print("Texto agregado correctamente.")

    elif opcion == '2':
        estado_anterior = historial.pop()

        if estado_anterior is not None:
            texto_actual = estado_anterior
            print("Operación deshecha correctamente.")
        else:
            print("No hay más acciones que deshacer.")

    elif opcion == '3':
        print("¡Gracias por utilizar nuestro programa!")
        break

    else:
        print(" ¡ERROR! Opción no válida. Inténtalo de nuevo.")