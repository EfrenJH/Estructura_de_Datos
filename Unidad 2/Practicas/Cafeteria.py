# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Cafetería.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import random
import time
import tracemalloc

class Pila:
    """Representa una estructura de datos LIFO (Last-In, First-Out)."""
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Cola:
    """Representa una estructura de datos FIFO (First-In, First-Out)."""
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# --- Inicio del ciclo principal del programa ---
while True:
    try:
        cantidad_clientes = int(input("¿Cuántos clientes comerán en la cafetería? "))

        if cantidad_clientes <= 0:
            print("Error: Debe haber al menos un cliente.")
            continue

        # --- Preparación de clientes y platillos ---
        
        # Los clientes se forman en una cola (FIFO)
        fila_clientes = Cola()
        for i in range(1, cantidad_clientes + 1):
            fila_clientes.enqueue(f"Cliente {i}")

        # Los platillos y bebidas se apilan (LIFO)
        pila_comida = Pila()
        tipos_de_platillo = ["Torta", "Quesadilla", "Dobladita"]
        tipos_de_bebida = ["Agua de Horchata", "Refresco", "Café"]
        
        # Generar una lista aleatoria de platillos y bebidas
        ordenes_a_preparar = []
        for _ in range(cantidad_clientes):
            platillo = random.choice(tipos_de_platillo)
            bebida = random.choice(tipos_de_bebida)
            ordenes_a_preparar.append(f"{platillo} y {bebida}")
        
        random.shuffle(ordenes_a_preparar) # Mezclar las órdenes

        for orden in ordenes_a_preparar:
            pila_comida.push(orden)

        print(f"\nSe han preparado {cantidad_clientes} combos de platillo y bebida.")
        print(f"Los clientes están formados en la fila.")

        print("\n--- Estado Antes de Servir ---")
        print(f"Fila de clientes: {fila_clientes.items}")
        print(f"Pila de órdenes: {pila_comida.items}")
        print("-" * 30)

        print("Comenzando a servir...\n")

        # --- Medición de Tiempo y Memoria ---
        tracemalloc.start()
        inicio_tiempo = time.perf_counter()

        # --- Proceso de Servir ---
        while not fila_clientes.is_empty():
            cliente_atendido = fila_clientes.dequeue()
            orden_servida = pila_comida.pop()
            print(f"{cliente_atendido} recibe: {orden_servida}")
        
        fin_tiempo = time.perf_counter()
        mem_actual, mem_max = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # --- Fin de la Medición ---

        print("\n--- Estado Final ---")
        print(f"Fila de clientes: {fila_clientes.items}")
        print(f"Pila de órdenes: {pila_comida.items}")
        print(" Todos los clientes han sido atendidos.")
        
        # --- Resultados de Rendimiento ---
        print("\n--- Resultados de Ejecución ---")
        print(f"  Tiempo de ejecución: {fin_tiempo - inicio_tiempo:.6f} segundos")
        print(f" Memoria actual usada: {mem_actual / 1024:.2f} KB")
        print(f" Memoria máxima usada: {mem_max / 1024:.2f} KB")

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")

    # --- Opción para repetir la simulación ---
    otra_vez = input("\n¿Deseas realizar otra simulación? (s/n): ")
    if otra_vez.lower() != 's':
        print("\n¡Gracias por visitar la cafetería! 👋")
        break
    print("\n" + "="*40 + "\n")