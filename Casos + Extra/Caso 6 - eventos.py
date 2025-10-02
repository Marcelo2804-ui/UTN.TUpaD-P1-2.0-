shows = []      
entradas = []   

while True:
    print("\nMenú:")
    print("1. Ingresar shows")
    print("2. Ingresar entradas por show")
    print("3. Mostrar shows/entradas")
    print("4. Consultar entradas de un show")
    print("5. Listar shows agotados")
    print("6. Agregar show")
    print("7. Actualizar entradas (vender/devolución)")
    print("8. Ver todos los shows")
    print("9. Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case '1':
            cant = input("¿Cuántos shows querés ingresar? ").strip()
            if not cant.isdigit():
                print("ERROR: Debe ingresar un número.")
                continue
            cant = int(cant)
            for i in range(cant):
                nombre = input(f"Ingrese nombre del show #{i+1}: ").strip()
                if nombre == "":
                    print("ERROR: El nombre no puede estar vacío.")
                    continue
                nombre = nombre.title()
                if nombre in shows:
                    print("ERROR: Ese show ya existe.")
                    continue
                shows.append(nombre)
                entradas.append(0)
                print(f"OK: '{nombre}' registrado con 0 entradas.")
        case '2':
            if not shows:
                print("No hay shows para asignar entradas. Use opción 1 o 6.")
                continue
            for i in range(len(shows)):
                valor = input(f"Entradas para '{shows[i]}': ").strip()
                if not valor.isdigit():
                    print("ERROR: Debe ingresar un número entero >= 0. Se cancela la carga.")
                    break
                valor = int(valor)
                entradas[i] = valor
            else:
                print("Entradas actualizadas.")
        case '3':
            if not shows:
                print("No hay shows cargados.")
                continue
            print("\nDisponibilidad:")
            for i in range(len(shows)):
                print(f"- {shows[i]}: {entradas[i]} entradas")
        case '4':
            if not shows:
                print("No hay shows cargados.")
                continue
            nombre = input("Nombre del show a consultar: ").strip().title()
            if nombre not in shows:
                print("Ese show no existe.")
            else:
                idx = shows.index(nombre)
                print(f"{nombre}: {entradas[idx]} entradas disponibles")
        case '5':
            if not shows:
                print("No hay shows cargados.")
                continue
            hay = False
            print("Shows agotados (0 entradas):")
            for i in range(len(shows)):
                if entradas[i] == 0:
                    print(f"- {shows[i]}")
                    hay = True
            if not hay:
                print("Ninguno.")
        case '6':
            nombre = input("Nombre del nuevo show: ").strip()
            if nombre == "":
                print("ERROR: El nombre no puede estar vacío.")
                continue
            nombre = nombre.title()
            if nombre in shows:
                print("ERROR: Ese show ya existe.")
                continue
            cant = input(f"Entradas iniciales para '{nombre}': ").strip()
            if not cant.isdigit():
                print("ERROR: Debe ingresar un número entero >= 0.")
                continue
            cant = int(cant)
            shows.append(nombre)
            entradas.append(cant)
            print(f"OK: '{nombre}' agregado con {cant} entradas.")
        case '7':
            if not shows:
                print("No hay shows cargados.")
                continue
            nombre = input("Show a actualizar (vender/devolución): ").strip().title()
            if nombre not in shows:
                print("Ese show no existe.")
                continue
            idx = shows.index(nombre)
            print(f"Stock actual de '{nombre}': {entradas[idx]} entradas")
            modo = input("Ingrese 'v' para vender o 'd' para devolución: ").strip().lower()
            if modo == 'v':
                cant = input("¿Cuántas entradas desea vender? ").strip()
                if not cant.isdigit():
                    print("ERROR: Debe ingresar un número entero > 0.")
                    continue
                cant = int(cant)
                if cant <= 0:
                    print("ERROR: Debe ser mayor que 0.")
                    continue
                if cant > entradas[idx]:
                    print("ERROR: No puede vender más de las disponibles.")
                    continue
                entradas[idx] -= cant
                print(f"Venta OK. Nuevo stock: {entradas[idx]}")
            elif modo == 'd':
                cant = input("¿Cuántas entradas desea devolver? ").strip()
                if not cant.isdigit():
                    print("ERROR: Debe ingresar un número entero > 0.")
                    continue
                cant = int(cant)
                if cant <= 0:
                    print("ERROR: Debe ser mayor que 0.")
                    continue
                entradas[idx] += cant
                print(f"Devolución OK. Nuevo stock: {entradas[idx]}")
            else:
                print("Opción inválida. Use 'v' o 'd'.")
        case '8':
            if not shows:
                print("No hay shows cargados.")
                continue
            print("\nTodos los shows:")
            for i in range(len(shows)):
                print(f"- {shows[i]}: {entradas[i]} entradas")
        case '9':
            print("Hasta luego.")
            break
        case _:
            print("Opción inválida. Ingrese un número del 1 al 9.")
