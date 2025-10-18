# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 3
# Menú Con Todas Las Opciones.py    Listas Ligadas (Doblemente Ligadas)
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Nodo:
    """
    Clase para representar un nodo individual de la lista doblemente ligada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    """
    Clase que implementa una lista doblemente ligada con todos los métodos de los ejercicios.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    # --- Métodos de construcción y recorrido ---
    def push_front(self, dato):
        """Inserta un elemento al inicio de la lista."""
        n = Nodo(dato)
        n.next = self.head # type: ignore
        if self.head:
            self.head.prev = n # type: ignore
        else: # Si la lista estaba vacía
            self.tail = n
        self.head = n

    def push_back(self, dato):
        """Inserta un elemento al final de la lista."""
        n = Nodo(dato)
        n.prev = self.tail # type: ignore
        if self.tail:
            self.tail.next = n # type: ignore
        else: # Si la lista estaba vacía
            self.head = n
        self.tail = n

    def forward(self):
        """Devuelve una lista con los elementos en orden, desde la cabeza a la cola."""
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out

    def backward(self):
        """Devuelve una lista con los elementos en orden inverso, desde la cola a la cabeza."""
        cur, out = self.tail, []
        while cur:
            out.append(cur.dato)
            cur = cur.prev
        return out

    # --- Métodos de búsqueda e inserción ---
    def find(self, valor):
        """Busca un valor y devuelve el primer nodo que lo contiene."""
        cur = self.head
        while cur:
            if cur.dato == valor:
                return cur
            cur = cur.next
        return None

    def insert_after(self, objetivo, dato):
        """Inserta un 'dato' nuevo después del nodo con el valor 'objetivo'."""
        nodo_objetivo = self.find(objetivo)
        if not nodo_objetivo:
            print(f" Advertencia: No se encontró el valor {objetivo}, no se insertó nada.")
            return False

        n = Nodo(dato)
        n.prev = nodo_objetivo # type: ignore
        n.next = nodo_objetivo.next

        if nodo_objetivo.next:
            nodo_objetivo.next.prev = n
        else: # El objetivo era el último nodo
            self.tail = n
        nodo_objetivo.next = n # type: ignore
        return True

    # --- Métodos de eliminación ---
    def remove_node(self, nodo):
        """Método auxiliar para desconectar y eliminar un nodo específico."""
        if not nodo:
            return
        if nodo.prev:
            nodo.prev.next = nodo.next
        else: # Se está eliminando la cabeza
            self.head = nodo.next

        if nodo.next:
            nodo.next.prev = nodo.prev
        else: # Se está eliminando la cola
            self.tail = nodo.prev
        
        nodo.prev = None
        nodo.next = None

    def remove_value(self, valor):
        """Busca la primera ocurrencia de un valor y la elimina."""
        nodo_a_eliminar = self.find(valor)
        if not nodo_a_eliminar:
            print(f" Advertencia: No se encontró el valor {valor}, no se eliminó nada.")
            return
        self.remove_node(nodo_a_eliminar)

    # --- Métodos de utilidad ---
    def __len__(self):
        """Permite usar len(lista) para obtener el número de nodos."""
        cur, c = self.head, 0
        while cur:
            c += 1
            cur = cur.next
        return c

    def k_from_end(self, k):
        """Devuelve el dato del k-ésimo nodo desde el final (k=1 es el último)."""
        if k <= 0:
            return None
        cur = self.tail
        i = 1
        while cur and i < k:
            cur = cur.prev
            i += 1
        return cur.dato if cur else None

    # --- Método para remover duplicados ---
    def remove_dups(self):
        """Elimina todos los valores duplicados, conservando la primera aparición."""
        vistos = set()
        cur = self.head
        while cur:
            if cur.dato in vistos:
                siguiente = cur.next
                self.remove_node(cur)
                cur = siguiente
            else:
                vistos.add(cur.dato)
                cur = cur.next
    
    # --- Método para imprimir la lista de forma amigable ---
    def __str__(self):
        """Permite imprimir la lista directamente con print()."""
        return str(self.forward())


#------------- MENÚ PRINCIPAL ------------------#
def mostrar_menu():
    """Imprime las opciones del menú en la consola."""
    print("\n╔═══════════════════════════════════════╗")
    print("║   MENU - LISTA DOBLEMENTE LIGADA    ║")
    print("╠═══════════════════════════════════════╣")
    print("║ 1.  Insertar al inicio (push_front)   ║")
    print("║ 2.  Insertar al final (push_back)     ║")
    print("║ 3.  Insertar después de un valor      ║")
    print("║ 4.  Eliminar un valor                 ║")
    print("║ 5.  Eliminar duplicados               ║")
    print("║ 6.  Mostrar lista (adelante)          ║")
    print("║ 7.  Mostrar lista (atrás)             ║")
    print("║ 8.  Mostrar longitud de la lista      ║")
    print("║ 9.  Buscar k-ésimo desde el final     ║")
    print("║ 10. Salir                             ║")
    print("╚═══════════════════════════════════════╝")

"""Función principal que ejecuta el menú interactivo."""
ld = ListaDoble()
# Datos iniciales para que la lista no esté vacía
ld.push_back(10)
ld.push_back(20)
ld.push_back(30)
ld.push_back(10)

while True:
    print(f"\nEstado actual de la lista: {ld}")
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            dato = int(input("Ingrese el dato a insertar al inicio: "))
            ld.push_front(dato)
            print(f" Dato {dato} insertado al inicio.")
        
        elif opcion == '2':
            dato = int(input("Ingrese el dato a insertar al final: "))
            ld.push_back(dato)
            print(f" Dato {dato} insertado al final.")

        elif opcion == '3':
            objetivo = int(input("Ingrese el valor después del cual quiere insertar: "))
            dato = int(input(f"Ingrese el nuevo dato a insertar después de {objetivo}: "))
            if ld.insert_after(objetivo, dato):
                print(f" Dato {dato} insertado correctamente.")

        elif opcion == '4':
            valor = int(input("Ingrese el valor que desea eliminar: "))
            ld.remove_value(valor)
            print(f" Intento de eliminación del valor {valor} completado.")

        elif opcion == '5':
            ld.remove_dups()
            print(" Duplicados eliminados.")

        elif opcion == '6':
            print(f"Recorrido hacia adelante: {ld.forward()}")

        elif opcion == '7':
            print(f"Recorrido hacia atrás: {ld.backward()}")

        elif opcion == '8':
            print(f"La longitud de la lista es: {len(ld)}")

        elif opcion == '9':
            k = int(input("Ingrese la posición (k) desde el final (ej: 1 es el último): "))
            resultado = ld.k_from_end(k)
            if resultado is not None:
                print(f"El {k}-ésimo elemento desde el final es: {resultado}")
            else:
                print(f" No se pudo encontrar el elemento en la posición {k} desde el final.")
        
        elif opcion == '10':
            print(" ¡Adiós! Saliendo del programa.")
            break
        
        else:
            print(" Opción no válida. Por favor, intente de nuevo.")
    
    except ValueError:
        print(" Error: Por favor, ingrese un número entero válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

