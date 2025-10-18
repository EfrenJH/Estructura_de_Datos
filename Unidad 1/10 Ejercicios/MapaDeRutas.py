# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Mapa de Rutas.py    Bloque de 10 Programas
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

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
            print(f"Error: Una o ambas ciudades ('{v1}', '{v2}') no existen.")

    def encontrar_todos_los_caminos(self, inicio, fin):
        caminos_encontrados = []

        def buscar_dfs(vertice_actual, camino_parcial):
            camino_parcial.append(vertice_actual)

            if vertice_actual == fin:
                caminos_encontrados.append(camino_parcial.copy())
            else:
                for vecino in self.ady[vertice_actual]:
                    if vecino not in camino_parcial:
                        buscar_dfs(vecino, camino_parcial)

            camino_parcial.pop()

        buscar_dfs(inicio, [])
        return caminos_encontrados

    def mostrar(self):
        if not self.ady:
            print("El mapa está vacío.")
            return
        print("\n--- Estructura del Mapa Actual ---")
        for ciudad, carreteras in self.ady.items():
            print(f"  {ciudad} -> {carreteras}")
        print("---------------------------------")


# --- Programa Principal con Menú ---
mapa = Grafo()
opcion = 0

while opcion != 5:
    print("\n" + "="*25)
    print("   CONSTRUCTOR DE MAPAS ")
    print("="*25)
    print("1. Agregar ciudad")
    print("2. Agregar carretera (conectar dos ciudades)")
    print("3. Encontrar todas las rutas entre dos ciudades")
    print("4. Mostrar mapa actual")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Por favor, ingresa un número.")
        continue

    if opcion == 1:
        ciudad = input("Ingresa el nombre de la nueva ciudad: ")
        mapa.agregar_vertice(ciudad)
        print(f" Ciudad '{ciudad}' agregada al mapa.")

    elif opcion == 2:
        ciudades_lista = list(mapa.ady.keys())
        if len(ciudades_lista) < 2:
            print(" Necesitas agregar al menos dos ciudades para crear una carretera.")
            continue

        print("\n-- Elige la primera ciudad --")
        for i, ciudad in enumerate(ciudades_lista):
            print(f"  {i+1}.- {ciudad}")

        try:
            choice1 = int(input("Selecciona el número de la primera ciudad: "))
            if not (1 <= choice1 <= len(ciudades_lista)):
                print(" Número fuera de rango.")
                continue
            ciudad1 = ciudades_lista[choice1 - 1]
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número.")
            continue

        print(f"\n-- ¿A dónde conecta la carretera de '{ciudad1}'? --")
        for i, ciudad in enumerate(ciudades_lista):
            print(f"  {i+1}.- {ciudad}")

        try:
            choice2 = int(input(f"Selecciona el número de la ciudad a conectar con {ciudad1}: "))
            if not (1 <= choice2 <= len(ciudades_lista)):
                print(" Número fuera de rango.")
                continue
            ciudad2 = ciudades_lista[choice2 - 1]
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número.")
            continue

        if ciudad1 == ciudad2:
            print("Error: Una ciudad no puede conectarse consigo misma.")
        else:
            mapa.agregar_arista(ciudad1, ciudad2)
            print(f" Carretera entre '{ciudad1}' y '{ciudad2}' agregada.")

    elif opcion == 3:
        origen = input("Ingresa la ciudad de origen: ")
        destino = input("Ingresa la ciudad de destino: ")

        if origen in mapa.ady and destino in mapa.ady:
            rutas_posibles = mapa.encontrar_todos_los_caminos(origen, destino)
            print(f"\n Rutas encontradas de {origen} a {destino}:")
            if rutas_posibles:
                for i, ruta in enumerate(rutas_posibles):
                    print(f"  Ruta {i+1}: {' -> '.join(ruta)}")
            else:
                print("No se encontraron rutas entre estas dos ciudades.")
        else:
            print(f"Error: La ciudad de origen ('{origen}') o destino ('{destino}') no existe en el mapa.")

    elif opcion == 4:
        mapa.mostrar()

    elif opcion == 5:
        print(" ¡Gracias por utilizar este programa! :P")

    else:
        print(" Opción no válida. Inténtalo de nuevo.")