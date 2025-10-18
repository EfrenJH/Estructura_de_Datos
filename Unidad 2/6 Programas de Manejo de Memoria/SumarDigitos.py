# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Sumar Digitos.py    6 programas de Manejo de Memoria
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import time
import tracemalloc

def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return sumarDigitosAux(n)

def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n // 10) + n % 10
    
tracemalloc.start()
inicio = time.perf_counter_ns()

resultado = sumarDigitos(7543)

fin = time.perf_counter_ns()
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"Suma de los dígitos: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()