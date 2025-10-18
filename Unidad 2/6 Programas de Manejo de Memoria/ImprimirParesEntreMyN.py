# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Imprimir Pares Entre M y N.py    6 programas de Manejo de Memoria
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import time
import tracemalloc

def imprimirparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m.")
    
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    
    imprimirparesEntreMyNAux(m, n)

def imprimirparesEntreMyNAux(m, n):
    if m > n:
        print()
    
    else:
        print(m, end = " ")
        imprimirparesEntreMyNAux(m + 2, n)

tracemalloc.start()       
inicio = time.perf_counter_ns()

imprimirparesEntreMyN(3,13)

fin = time.perf_counter_ns()
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"\nTiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()