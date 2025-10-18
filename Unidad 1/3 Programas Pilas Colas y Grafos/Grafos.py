#Instrituto Tecnológico de San Juan del Río
#Ingeniería en Sistemas Computacionales
#Estructura de Datos
#Unidad 1
#Grafos.py    3 Programas: Pilas, Colas y Grafos
#Docente: Domingo Rosales Alvarez
#Efrén Jacobo Hernández
#No. de control: 24590384

from collections import deque

class Grafo:
    def __init__(self):
        self.ady = {}

    def agregar_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = []

    def agregar_arista(self, v1, v2):
        if v1 in self.ady and v2 in self.ady:
            self.ady[v1].append(v2)
            self.ady[v2].append(v1)  # No dirigido

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(actual)
                cola.extend(self.ady[actual])

        return recorrido

    def dfs(self, inicio):
        visitados = set()
        recorrido = []

        def dfs_recursivo(nodo):
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                for vecino in self.ady[nodo]:
                    dfs_recursivo(vecino)

        dfs_recursivo(inicio)
        return recorrido


# Prueba
g = Grafo()
for v in ["A", "B", "C", "D", "E"]:
    g.agregar_vertice(v)

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")
g.agregar_arista("C", "E")

print("BFS desde A:", g.bfs("A"))  # ['A', 'B', 'C', 'D', 'E']
print("DFS desde A:", g.dfs("A"))  # ['A', 'B', 'D', 'C', 'E']