# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Cafetería Random.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

#ALGORITMO
#¿Qué resuelvo?
# - Asignar un platillo a cada cliente de la cafetería (Hay 3 tipos de platillos: Tortas, quesadillas y dobladitas) (Opcional: agregar bebidas)
#¿Qué necesito?
# - Conocer la cantidad de clientes que comerán en la cafetería

#¿Cómo lo resuelvo?
# - Pedir la cantida de clientes que comerán en la cafería
# - Colocar la misma cantidad de platillas de manera aleatoria (a cada cliente le corresponde un platillo)
import random

class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


while True:
    try:
        cantidad_clientes = int(input("¿Cuántos clientes comerán en la cafetería? "))

        if cantidad_clientes <= 0:
            print("Error: Debe haber al menos un cliente.")
            continue


        fila_clientes = Cola()
        for i in range(1, cantidad_clientes + 1):
            fila_clientes.enqueue(f"Cliente {i}")

        pila_platillos = Pila()
        tipos_de_platillo = ["Torta", "Quesadilla", "Dobladita"]
        platillos_a_preparar = [random.choice(tipos_de_platillo) for _ in range(cantidad_clientes)]
        random.shuffle(platillos_a_preparar)

        for platillo in platillos_a_preparar:
            pila_platillos.push(platillo)

        print(f"\nSe han preparado {cantidad_clientes} platillos.")
        print(f"Los clientes están formados en la fila.")

        print("\n--- Estado Antes de Servir ---")
        print(f"Fila de clientes: {fila_clientes.items}")
        print(f"Pila de platillos: {pila_platillos.items}")
        print("-" * 30)

        print("Comenzando a servir...\n")

        while not fila_clientes.is_empty():
            cliente_atendido = fila_clientes.dequeue()
            platillo_servido = pila_platillos.pop()

            print(f"{cliente_atendido} recibe: {platillo_servido}")

        print("\n--- Estado Final ---")
        print(f"Fila de clientes: {fila_clientes.items}")
        print(f"Pila de platillos: {pila_platillos.items}")
        print("Todos los clientes han sido atendidos.")

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")

    otra_vez = input("\n¿Deseas realizar otra simulación? (s/n): ")
    if otra_vez.lower() != 's':
        print("\n ¡Gracias por visitar la cafetería!")
        break
    print("\n" + "="*30 + "\n")