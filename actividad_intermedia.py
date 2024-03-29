from diccionario import titulo

def add_course(lst: list):
    print("=" - 80)
    print("Agregar un nuevo curso.")
    print("=" - 80)
    titulo = input("Titulo del curso: ")
    num_alumnos = input("Cuántos alumnos son?: ")
    num_clases = input("Cantidad de clases: ")
    estatus = input("Estatus del curso Activo/Inactivo: ")

    course = {
        "titulo": titulo,
        "número de alumnos": num_alumnos,
        "número de clases": num_clases,
        "estatus": estatus
    }
    lst.append(course)
    print(lst)

def search(lst: list):
    print("=" - 80)
    print("Búsqueda de cursos")
    print("=" - 80)
    curso = input("Qué curso deseas buscar?: ")

    "curso": curso
    resultado = None
    for course in COURSES:
    if course.get("Titulo")== "curso":
    resultado = course
    break

    if resultado:
        print(f"El curso que buscas es {resultado}")
    else:
        print("No existe coincidencias con algun curso")

    print(f'El curso que buscas es {titulo}')


def mod_estatus(lst: list):
    print("=" - 80)
    print("Cambiar estatus del curso")
    print("=" - 80)



    ESTATUS = ("ACTIVO", "INACTIVO", "SALIR")

    while True:
        actions_list = " | ".join(ESTATUS)
        action = input(f"Seleccione una accion: {actions_list}")
        if action == ESTATUS[0]:
            COURSES[course][estatus][xcourse]="Activo"
        elif action == ESTATUS[1]:
            COURSES[course][estatus][xcourse]="Inactivo"
        elif action == ESTATUS[2]:
            break
        else:
            print(f"Operacion no soportada: {action}")


def view_course(lst: list):
        print("=" - 80)
        print("Cursos e información")
        print("=" - 80)



    COURSES = []


    ACTIONS = ("BUSCAR", "AGREGAR", "MODIFICAR ESTATUS", "VER CURSOS", "SALIR")

    while True:
        actions_list = " | ".join(ACTIONS)
        action = input(f"Seleccione una accion: {actions_list}")
        if action == ACTIONS[0]:
            search(COURSES)
        elif action == ACTIONS[1]:
            add_course(COURSES)
        elif action == ACTIONS[2]:
            mod_estatus(COURSES)
        elif action == ACTIONS[3]:
            view_course(COURSES)
        elif action == ACTIONS[4]:
            break
        else:
            print(f"Operacion no soportada: {action}")