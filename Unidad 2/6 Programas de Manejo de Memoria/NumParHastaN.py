# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Numero Par Hasta N.py    6 Programas de Manejo de Memoria
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import time
import tracemalloc

def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo")
    n -= n % 2
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

tracemalloc.start()    

inicio = time.perf_counter_ns()      

imprimirParesHastaN(9)

fin = time.perf_counter_ns()

mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"\nTiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()