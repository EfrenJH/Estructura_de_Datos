# Instrituto Tecnológico de San Juan del Río
# Ingeniería en Sistemas Computacionales
# Estructura de Datos
# Unidad 2
# Banco.py    Ejercicios
# Docente: Domingo Rosales Alvarez
# Efrén Jacobo Hernández
# No. de control: 24590384

def simular_atencion_bancaria():
    
    fila_llegada_bidimensional = []
    
    print("--- Registro de Clientes en Fila de Llegada ---")
    for i in range(10):
        nombre = input(f"Ingrese el nombre del cliente {i + 1}: ")
        
        while True:
            try:
                prioridad = int(input(f"Prioridad para {nombre} (1: Inversión, 2: Cuenta, 3: Normal): "))
                if prioridad in [1, 2, 3]:
                    break
                else:
                    print("Error: La prioridad debe ser 1, 2 o 3.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        
        fila_llegada_bidimensional.append([nombre, prioridad])
    
    if not fila_llegada_bidimensional:
        print("\nNo hay clientes para atender.")
        return

    fila_atencion = []

    primer_cliente = fila_llegada_bidimensional[0]
    fila_atencion.append(primer_cliente)
    
    for i in range(1, len(fila_llegada_bidimensional)):
        cliente_actual = fila_llegada_bidimensional[i]
        nombre_actual, prioridad_actual = cliente_actual

        if prioridad_actual == 1:
            max_saltos = 3
        elif prioridad_actual == 2:
            max_saltos = 2
        else:
            max_saltos = 0
            
        saltos_realizados = 0
        posicion_insercion = len(fila_atencion)

        for j in range(len(fila_atencion) - 1, -1, -1):
            cliente_en_fila = fila_atencion[j]
            prioridad_en_fila = cliente_en_fila[1]
            
            if prioridad_actual < prioridad_en_fila and saltos_realizados < max_saltos:
                saltos_realizados += 1
                posicion_insercion = j
            else:
                posicion_insercion = j + 1
                break
        
        if posicion_insercion == 0:
            posicion_insercion = 1
        
        fila_atencion.insert(posicion_insercion, cliente_actual)

    fila_atencion_unidimensional = [f"{cliente[0]} (Prioridad {cliente[1]})" for cliente in fila_atencion]

    print("\n\n           RESULTADOS FINALES\n\n")
    
    print("\n## Arreglo 1: Fila de Llegada (Bidimensional)")
    print("Formato: [Nombre, Prioridad]")
    print(fila_llegada_bidimensional)
    
    print("\n## Arreglo 2: Fila de Atención Final (Unidimensional)")
    print("Formato: Nombre (Prioridad)")
    for i, cliente_str in enumerate(fila_atencion_unidimensional):
        print(f"{i + 1}. {cliente_str}")

simular_atencion_bancaria()