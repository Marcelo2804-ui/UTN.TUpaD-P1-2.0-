herramientas = [] 
existencias = []

opcion = ""
while opcion != "8":
    print("\nMENÚ")
    print("1) Ingresar herramientas")
    print("2) Ingresar existencias por herramienta")
    print("3) Mostrar existencias")
    print("4) Consultar disponibilidad por nombre")
    print("5) Listar agotados (stock = 0)")
    print("6) Agregar herramienta nueva")
    print("7) Actualizar existencias (venta / ingreso)")
    print("8) Salir")
    opcion = input("Elegí una opción (1-8): ").strip()

    match opcion:
        case "1":
            print("Carga de herramientas")
            cant_txt = input("¿Cuántas querés cargar? ").strip()
            if not cant_txt.isdigit():
                print("Número inválido. Ingresá un entero (0 o mayor).")
continue
            cant = int(cant_txt)
            if cant <= 0:
                print("No se cargaron herramientas.")
                continue
            i = 0
            while i < cant:
                nombre = input(f"Nombre #{i+1}: ").strip()
                if nombre == "":
                    print("El nombre no puede estar vacío.")
                    continue
                duplicada = False
                j = 0
                while j < len(herramientas):
                    if herramientas[j].lower() == nombre.lower():
                        duplicada = True
                        break
                    j += 1
                if duplicada:
                    print("Esa herramienta ya existe. Probá con otra.")
                    continue
                herramientas.append(nombre)
                existencias.append(0)  # por ahora 0, se que viene por defecto pero queria comentar algo profe.
                i += 1
            print("Herramientas cargadas.")
        case "2":
            if len(herramientas) == 0:
                print("Primero cargá herramientas (opción 1).")
                continue
            print("Carga/Actualización de existencias")
            idx = 0
            while idx < len(herramientas):
                nombre = herramientas[idx]
                stock_txt = input(f"Stock para '{nombre}': ").strip()
                if not stock_txt.isdigit():
                    print("Ingresá un entero válido (0 o mayor).")
                    continue
                stock = int(stock_txt)
                if stock < 0:
                    print("No se permiten negativos.")
                    continue
                existencias[idx] = stock
                idx += 1
            print("Existencias actualizadas.")
        case "3":
            print("\nInventario actual")
            if len(herramientas) == 0:
                print("(sin herramientas)")
            else:
                print("--------------------------------------")
                print("Herramienta".ljust(26), "Stock")
                print("--------------------------------------")
                k = 0
                while k < len(herramientas):
                    print(herramientas[k].ljust(26), existencias[k])
                    k += 1
                print("--------------------------------------")
        case "4":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
                continue
            buscado = input("Nombre a consultar: ").strip()
            if buscado == "":
                print("El nombre no puede estar vacío.")
                continue
            pos = -1
            k = 0
            while k < len(herramientas):
                if herramientas[k].lower() == buscado.lower():
                    pos = k
                    break
                k += 1
            if pos == -1:
                print(f"'{buscado}' no está en el catálogo.")
            else:
                print(f"Stock de '{herramientas[pos]}': {existencias[pos]}")
        case "5":
            # Listar herramientas con stock 0
            print("\nAgotados (stock = 0)")
            hay = False
            k = 0
            while k < len(herramientas):
                if existencias[k] == 0:
                    print(f"- {herramientas[k]}")
                    hay = True
                k += 1
            if not hay:
                print("(ninguna)")
        case "6":
            # Agregar herramienta nueva + su stock inicial
            print("Agregar herramienta")
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue
            duplicada = False
            k = 0
            while k < len(herramientas):
                if herramientas[k].lower() == nombre.lower():
                    duplicada = True
                    break
                k += 1
            if duplicada:
                print("Esa herramienta ya existe. Usá la opción 7 para actualizar su stock.")
                continue
            stock_txt = input("Stock inicial: ").strip()
            if not stock_txt.isdigit():
                print("Ingresá un entero válido (0 o mayor).")
                continue
            stock = int(stock_txt)
            if stock < 0:
                print("No se permiten negativos.")
                continue
            herramientas.append(nombre)
            existencias.append(stock)
            print(f"'{nombre}' agregada con {stock} unidades.")
        case "7":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
                continue
            print("\nActualizar existencias (venta / ingreso)")
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue
            pos = -1
            k = 0
            while k < len(herramientas):
                if herramientas[k].lower() == nombre.lower():
                    pos = k
                    break
                k += 1
            if pos == -1:
                print(f"'{nombre}' no está en el catálogo.")
                continue
            print("Operación: V) Venta  |  I) Ingreso")
            oper = input("Elegí (V/I): ").strip().lower()
            if oper not in ("v", "i"):
                print("Opción inválida. Usá 'V' o 'I'.")
                continue
            cant_txt = input("Cantidad: ").strip()
            if not cant_txt.isdigit():
                print("Ingresá un entero válido.")
                continue
            cant = int(cant_txt)
            if oper == "v":
                if cant <= 0:
                    print("La venta debe ser mayor a 0.")
                    continue
                if cant > existencias[pos]:
                    print(f"No podés vender {cant}; stock disponible: {existencias[pos]}.")
                    continue
                existencias[pos] = existencias[pos] - cant
                print(f"Venta registrada. Nuevo stock de '{herramientas[pos]}': {existencias[pos]}")
            else:
                if cant < 0:
                    print("No se permiten negativos.")
                    continue
                existencias[pos] = existencias[pos] + cant
                print(f"Ingreso registrado. Nuevo stock de '{herramientas[pos]}': {existencias[pos]}")
        case "8":
            print("Saliendo del sistema. Hasta luego.")
        case _:
            print("Opción inválida. Elegí un número del 1 al 8.")
