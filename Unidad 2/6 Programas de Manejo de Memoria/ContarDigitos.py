# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Contar Digitos.py    6 programas de Manejo de Memoria
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

import time
import tracemalloc

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1
    
tracemalloc.start()
inicio = time.perf_counter_ns()

resultado = contarDigitos(2574)

fin = time.perf_counter_ns()
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"Cantidad de dígitos: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()