"""
Menú interactivo
La aplicación debe mostrar un menú en la consola con opciones numéricas para que el usuario pueda elegir qué acción realizar.
Operaciones básicas:
Agregar una nueva tarea.
Listar todas las tareas con un indicador de estado (Pendiente o Completada).
Marcar una tarea como completada.
Eliminar una tarea.
Salir del programa.
Estructuras de datos
Utilizar diccionarios para representar cada tarea.
Usar una lista para almacenar todas las tareas.
Funciones
Dividir el código en funciones reutilizables para cada operación.
Validaciones y manejo de errores
Evitar errores al ingresar opciones no válidas.
Manejar archivos de manera segura para evitar pérdidas de datos.
"""
import time

tareas = []

def agregar_tarea(titulo, descripcion):
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    print(f"\nTarea '{titulo}' agregada exitosamente. <<<ÍNDICE: {len(tareas) }>>>")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")

def marcar_completada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print(f"Tarea '{tareas[indice]['titulo']}' marcada como completada.")
    else:
        print("Índice de tarea inválido.")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada['titulo']}' eliminada exitosamente.")
    else:
        print("Índice de tarea inválido.")

def mostrar_corazon_animado():
    arte = [
        "___________000000________________000000____________",
        "________00000000000___________000000000000_________",
        "______00000000____00000____000000_____0000000______",
        "____0000000_____________000______________00000_____",
        "___0000000_______________0_________________0000____",
        "__000000____________________________________0000___",
        "__00000_____________________________________0000___",
        "_00000______________________________________00000__",
        "_00000_____________________________________000000__",
        "__00000___________________________________000000___",
        "___00000_________________________________00000_____",
        "____000000______________________________00000______",
        "______00000___________________________00000________",
        "________0000_________________________0000__________",
        "__________0000______________________0000___________",
        "____________0000__________________0000_____________",
        "______________0000_______________000_______________",
        "_________________000____________00_________________",
        "___________________0000_______00___________________",
        "_____________________000____00_____________________",
        "_______________________00__0_______________________",
        "_________________________00________________________",
        "_______________________ _0_________________________",
        "________________________0__________________________",


    ]
    for linea in arte:
        print(linea)
        time.sleep(0.06)

def menu():
    while True:
        print("\n|||||||||||| MENU DE TAREAS ||||||||||||")
        print("1. Agregar nueva tarea")
        print("2. Ver todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("|"* 40)
        print(" ")

        opcion = input("Seleccione una opción: ")
        print(" ")
        print("|"* 40)

        
        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(titulo, descripcion)
        elif opcion == '2':
            listar_tareas()
        elif opcion == '3':
            if not tareas:
                print("No hay tareas para marcar como completadas.")
                continue
            indice = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
            marcar_completada(indice)
        elif opcion == '4':
            if not tareas:
                print("No hay tareas para eliminar.")
                continue
            indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            eliminar_tarea(indice)
        elif opcion == '5':
            print("Saliendo del programa, adiós.")
            mostrar_corazon_animado()
            print("Gracias por usar el gestor de tareas.")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")
menu()