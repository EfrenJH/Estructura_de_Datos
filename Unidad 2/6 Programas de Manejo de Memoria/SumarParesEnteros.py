# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Sumar Pares Enteros.py    6 programas de Manejo de Memoria
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import time
import tracemalloc

def sumarPares(n):
    if type(n) != int or n < 3:
        raise Exception("n debe ser entero mayor que 2.")
    n -= n % 2
    return sumarParesAux(n)

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n
    
tracemalloc.start()                     
inicio = time.perf_counter_ns()        

resultado = sumarPares(23)    

fin = time.perf_counter_ns()       
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"Suma de pares hasta N: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()