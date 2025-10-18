# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Aplanar.py    5 Programas de Recursividad
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

def aplanar(x: list) -> list[int]:
    if not x:
        return []
    
    cabeza, resto = x[0], x[1:]

    if isinstance(cabeza, int):
        return [cabeza] + aplanar(resto)
    
    return aplanar(cabeza) + aplanar(resto)

# Pruebas
assert aplanar([]) == []
assert aplanar([1,2,3]) == [1,2,3]
assert aplanar([1,[2,[3,4],5],[],6]) == [1,2,3,4,5,6]