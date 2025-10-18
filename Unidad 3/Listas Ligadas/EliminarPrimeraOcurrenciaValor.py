# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 3
# Eliminar Primera Ocurrecnia Valor.py    Listas Ligadas (Doblemente Ligadas)
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

"""
Ejercicio 3 — Eliminar primera ocurrencia por valor 
Enunciado: Implementa remove_value(v) que quite la primera ocurrencia de v. 
"""
def remove_node(self, nodo): 
    if not nodo: return 
    if nodo.prev: nodo.prev.next = nodo.next 
    else: self.head = nodo.next 
    if nodo.next: nodo.next.prev = nodo.prev 
    else: self.tail = nodo.prev 
    nodo.prev = nodo.next = None 
 
def remove_value(self, v): 
    nodo = self.find(v) 
    self.remove_node(nodo) 

#Casos borde: eliminar head, tail o único nodo. 
#Complejidad: O(n) por la búsqueda; el desenlace es O(1). 