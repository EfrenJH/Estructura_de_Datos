# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Simulador De Cajero Automatico.py    Bloque de 10 Programas
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def front(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

cola_banco = Cola()
opcion = 0

while opcion != 4:
    print(" - - - MENU PRINCIPAL - - -")
    print(f"Clientes en espera: {cola_banco.items}")
    print("1. Agregar cliente a la cola")
    print("2. Atender a todos los clientes")
    print("3. Eliminar la cola completa")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue

    if opcion == 1:
        nombre = input("Ingrese el nombre del cliente: ")
        cola_banco.enqueue(nombre)
        print(f"Cliente '{nombre}' agregado a la cola.")

    elif opcion == 2:
        if cola_banco.is_empty():
            print("¿No hay clientes en la cola para atender.")
        else:
            print("\n--- Iniciando atención de clientes ---")
            while not cola_banco.is_empty():
                cliente_actual = cola_banco.front()
                print(f"\nPasando a atender a: {cliente_actual}")

                opcion2 = 0
                while opcion2 != 4:
                    print("\n  -- SUBMENU DE OPERACIONES --")
                    print(f"  Cliente: {cliente_actual}")
                    print("  1. Retirar")
                    print("  2. Depositar")
                    print("  3. Consultar saldo")
                    print("  4. Finalizar atención")

                    try:
                        opcion2 = int(input("  Ingrese una operación: "))
                    except ValueError:
                        print("  Error: Ingrese un número válido.")
                        continue

                    if opcion2 == 1:
                        print(f"Retiro exitoso para {cliente_actual}.")
                    elif opcion2 == 2:
                        print(f"Depósito exitoso para {cliente_actual}.")
                    elif opcion2 == 3:
                        print(f"Saldo consultado por {cliente_actual}.")
                    elif opcion2 == 4:
                        cliente_atendido = cola_banco.dequeue()
                        print(f"Cliente '{cliente_atendido}' atendido. Pasando al siguiente...")
                    else:
                        print("Opción de operación inválida.")

            print("\n--- Todos los clientes han sido atendidos. Volviendo al menú principal. ---")
    elif opcion == 3:
        cola_banco.clear()
        print("La cola de clientes ha sido eliminada.")

    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 4.")