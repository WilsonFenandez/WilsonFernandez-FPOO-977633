# Lista para almacenar las actividades ingresadas
actividades = []

# Función para agregar una nueva actividad
def agregar_actividad():
    codigo = input("Ingrese el código de la actividad: ")
    descripcion = input("Ingrese la descripción de la actividad: ")
    nota = float(input("Ingrese la nota de la actividad (0 a 5): "))

    # Validar la categoría hasta obtener una entrada válida
    while True:
        tipo = input("Ingrese el tipo de actividad (1: Quiz, 2: Parcial, 3: Trabajo): ")
        if tipo in ['1', '2', '3']:
            break
        print("Tipo inválido. Intente de nuevo.")
    
    # Diccionario para traducir los números a tipos de actividades
    tipos = {'1': 'Quiz', '2': 'Parcial', '3': 'Trabajo'}
    
    # Agregar la actividad a la lista
    actividades.append({
        "Código": codigo,
        "Descripción": descripcion,
        "Nota": nota,
        "Tipo": tipos[tipo]
    })

# Función para mostrar todas las actividades ingresadas
def mostrar_actividades():
    if actividades:
        print("\nActividades registradas:")
        for actividad in actividades:
            print(f"Código: {actividad['Código']}, Descripción: {actividad['Descripción']}, Nota: {actividad['Nota']}, Tipo: {actividad['Tipo']}")
    else:
        print("No se han registrado actividades.")

# Programa principal
def gestion_actividades():
    print("Sistema de gestión de actividades académicas.")
    while True:
        agregar_actividad()  # Agregar una nueva actividad
        mostrar_actividades()  # Mostrar todas las actividades registradas
        
        # Preguntar si el usuario desea agregar más actividades o salir
        if input("\n¿Agregar otra actividad? (s/n): ").lower() != 's':
            print("Programa finalizado.")
            break

# Ejecutar el programa
gestion_actividades()
