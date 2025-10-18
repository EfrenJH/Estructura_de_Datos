# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Revision Si Es Palindromo.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

from collections import deque

def es_palindromo(texto: str) -> bool:
    pila = []
    cola = deque()

    for caracter in texto:
        if caracter.isalnum():  
            caracter_limpio = caracter.lower()
            pila.append(caracter_limpio)
            cola.append(caracter_limpio)
    
    if not pila: 
        print("El texto no contiene caracteres válidos.")
        return False

    while cola:  
        de_la_cola = cola.popleft() 
        
        de_la_pila = pila.pop()   
        
        if de_la_cola != de_la_pila:
            return False
            
    return True

frases_de_prueba = [
    "casa",
    "racecar",
    "anilina",
    "Hola", 
    "2345423"
    "Anita lava la tina",
]

for frase in frases_de_prueba:
    if es_palindromo(frase):
        print(f"  '{frase}' -> Sí es un palíndromo.")
    else:
        print(f"  '{frase}' -> No es un palíndromo.")