# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Cola Circular Par Turnos.py    Bloque de 10 Programas
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

    def is_empty(self):
        return len(self.items) == 0


juego_turnos = Cola()

print("--- CONFIGURACIÓN DE LA PARTIDA ---")
while True:
    nombre_jugador = input("Ingresa el nombre de un jugador (o escribe 'listo' para empezar): ")
    if nombre_jugador.lower() == 'listo':
        if not juego_turnos.is_empty():
            break
        else:
            print("Debes agregar al menos un jugador.")
    else:
        juego_turnos.enqueue(nombre_jugador)
        print(f"{nombre_jugador} se ha unido al juego.")


print("\n" + "="*5)
print("¡QUE EMPIECE EL JUEGO!")
print("="*5)

opcion = 0
while opcion != 3:
    print("\n--- Menú de Turnos ---")
    print(f"Próximos turnos: {juego_turnos.items}")
    print("1. Pasar al siguiente turno")
    print("2. Ver orden de turnos")
    print("3. Terminar juego")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

    if opcion == 1:
        if not juego_turnos.is_empty():
            jugador_actual = juego_turnos.dequeue()
            juego_turnos.enqueue(jugador_actual)
            print(f"\n▶¡Es el turno de: {jugador_actual}!")
            input("   (Presiona Enter para continuar...)")
        else:
            print("No hay jugadores en el juego.")
    elif opcion == 2:
        print(f"\nEl orden de turnos es: {juego_turnos.items}")
    elif opcion == 3:
        print("\n¡Juego terminado!")
    else:
        print("Opción no válida.")