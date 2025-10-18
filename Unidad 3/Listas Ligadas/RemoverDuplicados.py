# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 3
# Remover Duplicados.py    Listas Ligadas (Doblemente Ligadas)
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

"""
Ejercicio 5 — Remover duplicados en sitio 
Enunciado: Dada una lista doble, elimina duplicados dejando la primera aparición (in-place). 
Idea: Usa un conjunto vistos. Recorre de izquierda a derecha, si dato ya está en vistos, elimina el 
nodo; si no, agrégalo.
"""
def remove_dups(self): 
    vistos = set() 
    cur = self.head 
    while cur: 
        if cur.dato in vistos: 
            borrar = cur 
            cur = cur.next 
            self.remove_node(borrar) 
        else: 
            vistos.add(cur.dato) 
            cur = cur.next 

#Complejidad: O(n) tiempo promedio, O(n) espacio por el set. Alternativa sin memoria extra: O(n²). 