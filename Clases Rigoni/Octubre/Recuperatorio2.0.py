# Inventario de Ferretería - Programación 1
# NOTA: sin funciones, sin try/except, sin diccionarios ni estructuras raras.
# Uso listas paralelas: herramientas[i] va con existencias[i].
# El menú queda con while + match/case como pide la consigna.

print("Sistema de Inventario (Ferretería)")
print("Primero conviene cargar herramientas (1) y después sus existencias (2).")

herramientas = []   # nombres simples
existencias = []    # stock (enteros >= 0)

opcion = ""   # arranco vacío para entrar al while

# Menú principal (queda hasta que el usuario elija salir con 8)
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
            # Cargar nombres iniciales. Por ahora el stock queda en 0 hasta la opción 2.
            print("\nCarga de herramientas")
            cant_txt = input("¿Cuántas querés cargar? ").strip()

            # No uso excepciones, así que valido a mano con isdigit()
            # Ojo: isdigit() no acepta negativos, pero justo no necesitamos negativos.
            if not cant_txt.isdigit():
                print("Número inválido. Ingresá un entero (0 o mayor).")
                # Podría reintentar en un bucle, pero prefiero volver al menú.
                continue

            cant = int(cant_txt)
            if cant <= 0:
                print("No se cargaron herramientas.")
                continue

            i = 0
            while i < cant:
                nombre = input(f"Nombre {i+1}: ").strip()

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
                existencias.append(0)   
                i += 1

            print("Herramientas cargadas.")

        case "2":
            if len(herramientas) == 0:
                print("Primero cargá herramientas (opción 1).")
                continue

            print("Carga/Actualización de existencias (en orden)")
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
                k = 0
                while k < len(herramientas):
                    print(herramientas[k].ljust(26), existencias[k])
                    k += 1

        case "4":
            # Buscar por nombre y mostrar la cantidad. Búsqueda lineal, simple.
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
            print("\nAgotados (stock = 0)")
            hay_agotados = False
            k = 0
            while k < len(herramientas):
                if existencias[k] == 0:
                    print(f"- {herramientas[k]}")
                    hay_agotados = True
                k += 1

            if not hay_agotados:
                print("(ninguna)")

        case "6":
            print("\nAgregar herramienta")
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

            print("Operación: V) Venta  |  I) Ingreso")
            oper = input("Elegí (V/I): ").strip().lower()
            if oper != "v" and oper != "i":
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
                # Si está todo bien, resto
                existencias[pos] = existencias[pos] - cant
                print(f"Venta registrada. Nuevo stock de '{herramientas[pos]}': {existencias[pos]}")
            else:
                if cant < 0:
                    print("No se permiten negativos en ingreso.")
                    continue
                existencias[pos] = existencias[pos] + cant
                print(f"Ingreso registrado. Nuevo stock de '{herramientas[pos]}': {existencias[pos]}")

        case "8":
            print("Saliendo del sistema. Hasta luego.")

        case _:
            print("Opción inválida. Elegí un número del 1 al 8.")