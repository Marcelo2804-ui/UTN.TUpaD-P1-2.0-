libros = ["Metamorfosis", "Programando con Rigoni", "Sufriendo las Matematicas de Mut", "Practicando con Hualpa"]
ejemplares = [0, 1, 2, 3]

while True:
    print('\n1. Ingresar titulos')
    print('2. Ingresar ejemplares por titulo')
    print('3. Mostrar catalogo')
    print('4. Consultar disponibilidad')
    print('5. Ver agotados')
    print('6. Agregar titulo')
    print('7. Actualizar ejemplares (prestamo/devolucion)')
    print('8. Salir')

    op = input('\nOpcion: ').strip()
    if not op.isdigit():
        print('Opcion invalida')
        continue
    opcion = int(op)

    if opcion == 1:
        cant_str = input('Cuantos titulos vas a ingresar?: ').strip()
        if cant_str.isdigit():
            cant = int(cant_str)
            if cant > 0:
                i = 0
                while i < cant:
                    t = input('Titulo: ').strip()
                    if len(t) == 0:
                        print('El titulo no puede ser vacio')
                    else:
                        existe = False
                        j = 0
                        while j < len(libros):
                            if libros[j].lower() == t.lower():
                                existe = True
                            j += 1
                        if existe:
                            print('Ya existe')
                        else:
                            libros.append(t)
                            ejemplares.append(0)
                    i += 1
            else:
                print('Cantidad invalida')
        else:
            print('Cantidad invalida')

    elif opcion == 2:
        if len(libros) == 0:
            print('No hay titulos')
        else:
            i = 0
            while i < len(libros):
                ok = False
                while not ok:
                    c = input('Ejemplares para "' + libros[i] + '": ').strip()
                    if c.isdigit():
                        n = int(c)
                        if n >= 0:
                            ejemplares[i] = n
                            ok = True
                        else:
                            print('No negativo')
                    else:
                        print('Ingrese un entero (0 o mayor)')
                i += 1

    elif opcion == 3:
        if len(libros) == 0:
            print('No hay libros')
        else:
            i = 0
            while i < len(libros):
                print(libros[i] + ': ' + str(ejemplares[i]) + ' ejemplares')
                i += 1

    elif opcion == 4:
        if len(libros) == 0:
            print('No hay titulos')
        else:
            b = input('Titulo a consultar: ').strip()
            if len(b) == 0:
                print('El titulo no puede ser vacio')
            else:
                idx = -1
                i = 0
                while i < len(libros):
                    if libros[i].lower() == b.lower():
                        idx = i
                    i += 1
                if idx == -1:
                    print('No existe')
                else:
                    print('"' + libros[idx] + '" -> ' + str(ejemplares[idx]) + ' disponibles')

    elif opcion == 5:
        if len(libros) == 0:
            print('No hay titulos')
        else:
            hay = False
            i = 0
            while i < len(libros):
                if ejemplares[i] == 0:
                    print(libros[i])
                    hay = True
                i += 1
            if not hay:
                print('No hay agotados')

    elif opcion == 6:
        nuevo = input('Titulo nuevo: ').strip()
        if len(nuevo) == 0:
            print('El titulo no puede ser vacio')
        else:
            dup = False
            i = 0
            while i < len(libros):
                if libros[i].lower() == nuevo.lower():
                    dup = True
                i += 1
            if dup:
                print('Ya existe')
            else:
                c = input('Ejemplares iniciales: ').strip()
                if c.isdigit():
                    n = int(c)
                    if n < 0:
                        n = 0
                else:
                    n = 0
                libros.append(nuevo)
                ejemplares.append(n)
                print('Agregado')

    elif opcion == 7:
        if len(libros) == 0:
            print('No hay titulos')
        else:
            nombre = input('Titulo: ').strip()
            if len(nombre) == 0:
                print('El titulo no puede ser vacio')
            else:
                idx = -1
                i = 0
                while i < len(libros):
                    if libros[i].lower() == nombre.lower():
                        idx = i
                    i += 1
                if idx == -1:
                    print('No existe')
                else:
                    print('1) Prestamo  2) Devolucion')
                    t = input('Opcion: ').strip()
                    if t.isdigit():
                        tipo = int(t)
                        if tipo == 1 or tipo == 2:
                            c = input('Cantidad: ').strip()
                            if c.isdigit():
                                cant = int(c)
                                if cant > 0:
                                    if tipo == 1:
                                        if cant <= ejemplares[idx]:
                                            ejemplares[idx] = ejemplares[idx] - cant
                                            print('OK, nuevo stock:', ejemplares[idx])
                                        else:
                                            print('No alcanza el stock')
                                    else:
                                        ejemplares[idx] = ejemplares[idx] + cant
                                        print('OK, nuevo stock:', ejemplares[idx])
                                else:
                                    print('Cantidad invalida')
                            else:
                                print('Cantidad invalida')
                        else:
                            print('Opcion invalida')
                    else:
                        print('Opcion invalida')

    elif opcion == 8:
        print('Saliendo...')
        break

    else:
        print('Opcion invalida')
