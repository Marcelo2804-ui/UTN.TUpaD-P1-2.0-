alumnos = []
asistencias = []

while True:
    print("\nMenú:")
    print("1. Ingresar estudiantes")
    print("2. Mostrar listado con asistencias")
    print("3. Consultar asistencias por estudiante")
    print("4. Listar estudiantes con asistencia 0")
    print("5. Agregar estudiante")
    print("6. Marcar asistencia")
    print("7. Ver todos")
    print("8. Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case '1':
            cant = input("¿Cuántos estudiantes desea ingresar? ").strip()
            if not cant.isdigit():
                print("ERROR: Debe ingresar un número.")
                continue
            cant = int(cant)
            for i in range(cant):
                nombre = input(f"Ingrese nombre del estudiante #{i+1}: ").strip()
                if nombre == "":
                    print("ERROR: El nombre no puede estar vacío.")
                    continue
                nombre = nombre.title()
                if nombre in alumnos:
                    print("ERROR: Ese estudiante ya existe.")
                    continue
                alumnos.append(nombre)
                asistencias.append(0)
                print(f"OK: {nombre} agregado con 0 asistencias.")

        case '2':
            if not alumnos:
                print("No hay estudiantes cargados.")
                continue
            for i in range(len(alumnos)):
                print(f"{alumnos[i]}: {asistencias[i]} asistencias")

        case '3':
            if not alumnos:
                print("No hay estudiantes cargados.")
                continue
            nombre = input("Nombre del estudiante: ").strip().title()
            if nombre not in alumnos:
                print("Ese estudiante no existe.")
            else:
                idx = alumnos.index(nombre)
                print(f"{nombre}: {asistencias[idx]} asistencias")

        case '4':
            if not alumnos:
                print("No hay estudiantes cargados.")
                continue
            hay = False
            for i in range(len(alumnos)):
                if asistencias[i] == 0:
                    print(f"- {alumnos[i]}")
                    hay = True
            if not hay:
                print("Ninguno.")

        case '5':
            nombre = input("Nombre del nuevo estudiante: ").strip()
            if nombre == "":
                print("ERROR: El nombre no puede estar vacío.")
                continue
            nombre = nombre.title()
            if nombre in alumnos:
                print("ERROR: Ese estudiante ya existe.")
                continue
            alumnos.append(nombre)
            asistencias.append(0)
            print(f"OK: {nombre} agregado con 0 asistencias.")

        case '6':
            if not alumnos:
                print("No hay estudiantes cargados.")
                continue
            nombre = input("Nombre del estudiante: ").strip().title()
            if nombre not in alumnos:
                print("Ese estudiante no existe.")
                continue
            idx = alumnos.index(nombre)
            asistencias[idx] += 1
            print(f"Asistencia marcada. Total: {asistencias[idx]}")

        case '7':
            if not alumnos:
                print("No hay estudiantes cargados.")
                continue
            for i in range(len(alumnos)):
                print(f"{alumnos[i]}: {asistencias[i]} asistencias")

        case '8':
            print("Hasta luego.")
            break

        case _:
            print("Opción inválida.")