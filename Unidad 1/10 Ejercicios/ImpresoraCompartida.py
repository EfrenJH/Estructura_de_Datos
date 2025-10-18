# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 1
# Impresora Compartida.py    Bloque de 10 Programas
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        """Agrega un documento a la cola de impresión."""
        self.items.append(dato)

    def dequeue(self):
        """Saca el siguiente documento de la cola para imprimirlo."""
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        """Verifica si no hay documentos en espera."""
        return len(self.items) == 0

cola_impresion = Cola()
opcion = 0

while opcion != 3:
    print(" - - -COLA DE IMPRESIÓN - - -")
    print(f"Documentos en espera: {len(cola_impresion.items)}")
    print("\n--- MENÚ ---")
    print("1. Enviar un documento a imprimir")
    print("2. Iniciar proceso de impresión")
    print("3. Apagar impresora (Salir)")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

    if opcion == 1:
        usuario = input("Ingresa tu nombre de usuario: ")
        nombre_archivo = input("Ingresa el nombre del archivo (ej: Tarea.docx): ")

        documento = {
            "usuario": usuario,
            "archivo": nombre_archivo
        }

        cola_impresion.enqueue(documento)
        print(f"Documento '{nombre_archivo}' de '{usuario}' ha sido agregado a la cola.")

    elif opcion == 2:
        if cola_impresion.is_empty():
            print("No hay documentos en la cola de impresión.")
        else:
            print("\n--- Iniciando trabajos de impresión ---")
            while not cola_impresion.is_empty():
                documento_a_imprimir = cola_impresion.dequeue()
                usuario = documento_a_imprimir["usuario"]
                archivo = documento_a_imprimir["archivo"]

                print(f"\n▶Imprimiendo '{archivo}' enviado por '{usuario}'...")
                print(f"¡Impresión de '{archivo}' completada!")
            print("\n--- Todos los documentos han sido impresos. ---")

    elif opcion == 3:
        print("Apagando la impresora...")

    else:
        print("Opción no válida.")