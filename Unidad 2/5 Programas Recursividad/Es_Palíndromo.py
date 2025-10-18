# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Es Palíndromo.py    5 Programas de Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

def es_palindromo(s: str) -> bool:
    """
    Verifica recursivamente si s es palíndromo (exacto; sensible a espacios y mayúsculas).
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])

def es_palindromo_normalizado(s: str) -> bool:
    t = "".join(ch.lower() for ch in s if not ch.isspace())
    return es_palindromo(t)

# Pruebas
assert es_palindromo("reconocer") is True
assert es_palindromo("python") is False
assert es_palindromo("") is True
assert es_palindromo("a") is True
assert es_palindromo_normalizado("Anita lava la tina") is True