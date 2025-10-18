#Instrituto Tecnológico de San Juan del Río
#Ingeniería en Sistemas Computacionales
#Estructura de Datos
#Unidad 1
#Pilas.py    3 Programas: Pilas, Colas y Grafos
#Docente: Domingo Rosales Alvarez
#Efrén Jacobo Hernández
#No. de control: 24590384

class Pila: 
    def __init__(self): 
        self.items = [] 
    
    def push(self, dato): 
        self.items.append(dato) 
    
    def pop(self): 
        return self.items.pop() if not self.is_empty() else None 
    
    def is_empty(self): 
        return len(self.items) == 0 

def es_palindromo(palabra): 
    pila = Pila() 
    for letra in palabra: 
        pila.push(letra) 
    
    invertida = "" 
    while not pila.is_empty():
        invertida += pila.pop()  # type: ignore
    
    return palabra == invertida 

# Prueba 
print(es_palindromo("radar"))   # True 
print(es_palindromo("python"))  # False 

