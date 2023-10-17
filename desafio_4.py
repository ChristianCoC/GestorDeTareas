# GESTOR DE TAREAS EN PYTHON
# Creado por: Christian Siles.
'''
Descripción:
Este proyecto consistirá en desarrollar una herramienta de gestión de tareas, 
donde los usuarios puedan crear y editar tareas de una lista.
Entregables:
Tendrán que entregar el código de Python que implemente las funcionalidades de gestión de tareas: 
crear, editar tareas de una lista. 
La función recibirá como parámetro una lista y realizará las modificaciones correspondientes.
'''

# Agregar tarea
def agregar_tarea(lista, tarea):
    lista.append(tarea)

# Editar tarea
def editar_tarea(lista, indice, nueva_tarea):
    if indice > 0 and indice < len(lista):
        lista[indice] = nueva_tarea
    elif indice < 0 or indice > len(lista):
        print("Índice no válido, ingrese el indice de la tarea.")

# Eliminar tarea
def eliminar_tarea(lista, indice):
    if indice > 0 and indice < len(lista):
        del lista[indice]
    else:
        print("Índice no válido, la tarea no pudo ser eliminada.")

# Mostrar lista de tareas
def listar_tareas(lista):
    if len(lista) == 0:
        print("No hay tareas para mostrar.")
    else:
        for i, tarea in enumerate(lista):
            print(f"{i + 1}.{tarea}")

# Ejecución del programa
tareas = []
while True:
    print("----------------")
    print("GESTOR DE TAREAS")
    print("----------------")
    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas, tarea)
    elif opcion == "2":
        listar_tareas(tareas)
        indice = int(input("Ingrese el índice de la tarea que desea editar: "))-1
        if indice > 0 and indice < len(tareas):
            nueva_tarea = input("Ingrese la nueva descripción de la tarea: ")
            editar_tarea(tareas, indice, nueva_tarea)
        else:
            print("Índice no válido, ingrese el indice de la tarea.")
    elif opcion == "3":
        listar_tareas(tareas)
        indice = int(input("Ingrese el índice de la tarea que desea eliminar: "))-1
        eliminar_tarea(tareas, indice)
    elif opcion == "4":
        listar_tareas(tareas)
    elif opcion == "5":
        print("Gracias por usar el gestor de tareas!!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

