# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Factorial.py    5 Programas de Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

def factorial(n: int) -> int:
  """
  Calcula n! recursivamente.
  Precondición: n >= 0
  """
  if n < 0:
    raise ValueError("factorial: n debe ser >= 0")
  if n == 0 or n == 1:
    return 1
  return n * factorial(n - 1)

# Pruebas
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
     