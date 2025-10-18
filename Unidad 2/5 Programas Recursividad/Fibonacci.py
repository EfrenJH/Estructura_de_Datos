# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Fibonacci.py    5 Programas de Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo_memo(n: int, memo=None) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if memo is None:
        memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]

# Pruebas
assert fibo(0) == 0 and fibo(1) == 1 and fibo(7) == 13
assert fibo_memo(0) == 0 and fibo_memo(1) == 1 and fibo_memo(30) == 832040