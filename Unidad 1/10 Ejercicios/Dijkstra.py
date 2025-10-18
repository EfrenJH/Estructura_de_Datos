# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Dijkstra En Grafo Ponderado.py    Bloque de 10 Programas
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class GrafoPonderado:
    def __init__(self):
        self.ady = {}

    def agregar_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = []

    def agregar_arista(self, v1, v2, km):
        if v1 in self.ady and v2 in self.ady:
            self.ady[v1].append((v2, km))
            self.ady[v2].append((v1, km))
        else:
            print("Error: Una o ambas ciudades no existen.")

    def mostrar(self):
        if not self.ady:
            print("El mapa está vacío.")
            return
        print("\n--- Estructura del Mapa Actual ---")
        for ciudad, carreteras in self.ady.items():
            print(f"  {ciudad} -> {carreteras}")
        print("---------------------------------")

    def dijkstra(self, origen):
        if origen not in self.ady:
            return None

        distancias = {vertice: float('infinity') for vertice in self.ady}
        distancias[origen] = 0
        visitados = set()

        for _ in range(len(self.ady)):
            vertice_actual = None
            distancia_minima = float('infinity')

            for vertice, distancia in distancias.items():
                if distancia < distancia_minima and vertice not in visitados:
                    distancia_minima = distancia
                    vertice_actual = vertice

            if vertice_actual is None:
                break

            visitados.add(vertice_actual)

            for vecino, km_arista in self.ady[vertice_actual]:
                distancia_nueva = distancias[vertice_actual] + km_arista

                if distancia_nueva < distancias[vecino]:
                    distancias[vecino] = distancia_nueva

        return distancias

mapa = GrafoPonderado()
opcion = 0

while opcion != 5:
    print("\n" + "="*35)
    print("  CALCULADORA DE RUTAS (DIJKSTRA)")
    print("="*35)
    print("1. Agregar ciudad")
    print("2. Agregar carretera (con distancia)")
    print("3. Calcular distancias más cortas")
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
            try:
                km = int(input(f"Ingresa la distancia (km) entre '{ciudad1}' y '{ciudad2}': "))
                mapa.agregar_arista(ciudad1, ciudad2, km)
                print(f"Carretera entre '{ciudad1}' y '{ciudad2}' con distancia {km} agregada.")
            except ValueError:
                print("Error: La distancia debe ser un número.")

    elif opcion == 3:
        ciudades_lista = list(mapa.ady.keys())
        if not ciudades_lista:
            print("No hay ciudades en el mapa para calcular rutas.")
            continue

        print("\n-- Elige la ciudad de origen --")
        for i, ciudad in enumerate(ciudades_lista):
            print(f"  {i+1}.- {ciudad}")

        try:
            choice = int(input("Selecciona el número de la ciudad de origen: "))
            if not (1 <= choice <= len(ciudades_lista)):
                print("Número fuera de rango.")
                continue
            ciudad_origen = ciudades_lista[choice - 1]
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")
            continue

        distancias_minimas = mapa.dijkstra(ciudad_origen)

        print(f"\nLas distancias más cortas desde '{ciudad_origen}':")
        if distancias_minimas:
            for ciudad, distancia in distancias_minimas.items():
                if distancia == float('infinity'):
                    print(f"  - A '{ciudad}': No hay ruta disponible.")
                else:
                    print(f"  - A '{ciudad}': {distancia}")
        else:
            print("No se pudo calcular. Asegúrate de que la ciudad de origen existe.")

    elif opcion == 4:
        mapa.mostrar()

    elif opcion == 5:
        print(" ¡Gracias por utilizar este programa! :P.")

    else:
        print("Opción no válida.")