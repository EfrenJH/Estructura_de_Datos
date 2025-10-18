# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Camino Más Corto BFS.py    Bloque de 10 Programas
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

from collections import deque

class Grafo:
    def __init__(self):
        self.ady = {}

    def agregar_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = []

    def agregar_arista(self, v1, v2):
        if v1 in self.ady and v2 in self.ady:
            if v2 not in self.ady[v1]:
                self.ady[v1].append(v2)
            if v1 not in self.ady[v2]:
                self.ady[v2].append(v1)
        else:
            print(f"Error: Una o ambas ciudades no existen.")

    def mostrar(self):
        if not self.ady:
            print("El mapa está vacío.")
            return
        print("\n--- Estructura del Mapa Actual ---")
        for ciudad, carreteras in self.ady.items():
            print(f"  {ciudad} -> {carreteras}")
        print("---------------------------------")

    def bfs_camino_corto(self, inicio, fin):
        if inicio not in self.ady or fin not in self.ady:
            return None

        cola = deque([[inicio]])
        visitados = {inicio}

        while cola:
            camino_actual = cola.popleft()
            ultimo_nodo = camino_actual[-1]

            if ultimo_nodo == fin:
                return camino_actual

            for vecino in self.ady[ultimo_nodo]:
                if vecino not in visitados:
                    nuevo_camino = list(camino_actual)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)
                    visitados.add(vecino)

        return None

mapa = Grafo()
opcion = 0

while opcion != 5:
    print("\n" + "="*28)
    print("  BUSCADOR DE RUTAS CORTAS")
    print("="*28)
    print("1. Agregar ciudad")
    print("2. Agregar carretera")
    print("3. Encontrar la ruta más corta")
    print("4. Mostrar mapa actual")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Ingresa un número.")
        continue

    if opcion == 1:
        ciudad = input("Ingresa el nombre de la nueva ciudad: ")
        mapa.agregar_vertice(ciudad)
        print(f"Ciudad '{ciudad}' agregada al mapa.")

    elif opcion == 2:
        ciudades_lista = list(mapa.ady.keys())
        if len(ciudades_lista) < 2:
            print("Necesitas al menos dos ciudades para crear una carretera.")
            continue

        print("\n-- Elige la primera ciudad --")
        for i, ciudad in enumerate(ciudades_lista):
            print(f"  {i+1}.- {ciudad}")

        try:
            choice1 = int(input("Selecciona el número: "))
            if not (1 <= choice1 <= len(ciudades_lista)):
                print("Número fuera de rango.")
                continue
            ciudad1 = ciudades_lista[choice1 - 1]
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            continue

        print(f"\n-- Elige la ciudad a conectar con '{ciudad1}' --")
        for i, ciudad in enumerate(ciudades_lista):
            print(f"  {i+1}.- {ciudad}")

        try:
            choice2 = int(input("Selecciona el número: "))
            if not (1 <= choice2 <= len(ciudades_lista)):
                print("Número fuera de rango.")
                continue
            ciudad2 = ciudades_lista[choice2 - 1]
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            continue

        if ciudad1 == ciudad2:
            print("Error: Una ciudad no puede conectarse consigo misma.")
        else:
            mapa.agregar_arista(ciudad1, ciudad2)
            print(f"Carretera entre '{ciudad1}' y '{ciudad2}' agregada.")

    elif opcion == 3:
        origen = input("Ingresa la ciudad de origen: ")
        destino = input("Ingresa la ciudad de destino: ")

        ruta_corta = mapa.bfs_camino_corto(origen, destino)

        print(f"\nLa ruta más corta de {origen} a {destino} es:")
        if ruta_corta:
            print(f"  {' -> '.join(ruta_corta)}")
            print(f"  Distancia: {len(ruta_corta) - 1} carreteras.")
        else:
            print("No se encontraron rutas entre estas dos ciudades.")

    elif opcion == 4:
        mapa.mostrar()

    elif opcion == 5:
        print(" ¡Gracias por utilizar este programa! :P.")

    else:
        print("Opción no válida.")