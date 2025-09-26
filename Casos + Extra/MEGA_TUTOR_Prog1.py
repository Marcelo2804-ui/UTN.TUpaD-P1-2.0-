# MEGA PY - Tutor interactivo Programacion 1 (UTN TUPaD)
# Estilo simple, sin tildes, while + if/elif, listas paralelas, validaciones con .isdigit()
# Autor: (completar)

# Banner inicial
print('\nTUTOR PROG1 - MEGA PY')
print('----------------------')
print('Aprender por secciones, con ejemplos y mini practicas.')

# Variables auxiliares
salir_total = False

while not salir_total:
    print('\nMENU PRINCIPAL')
    print('1. Variables y tipos + IO')
    print('2. Operadores')
    print('3. Condicionales (if/elif/else)')
    print('4. Bucles (while)')
    print('5. match/case (Python 3.10+)')
    print('6. Listas')
    print('7. Listas paralelas')
    print('8. Validaciones sin excepciones (.isdigit)')
    print('9. Menu persistente (plantilla)')
    print('10. Caso practico: Biblioteca (listas paralelas)')
    print('11. Quiz rapido (10 preguntas)')
    print('12. Salir')

    op = input('\nOpcion: ').strip()
    if not op.isdigit():
        print('Opcion invalida')
        continue
    opcion = int(op)

    if opcion == 1:
        print('\n--- 1) VARIABLES, TIPOS, IO ---')
        print('int, float, str. input lee texto. print muestra.')
        print('Ejemplo:')
        print('  nombre = input("Nombre: ")')
        print('  edad_str = input("Edad: ")  # texto')
        print('  if edad_str.isdigit(): edad = int(edad_str)')
        print('  print("Hola", nombre, "edad:", edad)')
        print('\nDemo rapida:')
        nombre = input('Nombre: ').strip()
        edad_txt = input('Edad: ').strip()
        if edad_txt.isdigit():
            edad = int(edad_txt)
            print('Hola', nombre, 'edad:', edad)
        else:
            print('Edad invalida')
        input('\nEnter para seguir...')

    elif opcion == 2:
        print('\n--- 2) OPERADORES ---')
        print('Aritmeticos: +, -, *, /, //, %, **')
        print('Comparacion: ==, !=, <, >, <=, >=')
        print('Logicos: and, or, not')
        print('\nDemo: suma y comparacion')
        a_txt = input('a: ').strip()
        b_txt = input('b: ').strip()
        if a_txt.isdigit() and b_txt.isdigit():
            a = int(a_txt)
            b = int(b_txt)
            print('a+b=', a+b)
            print('a==b?', a==b)
            print('a>b?', a>b)
        else:
            print('Datos invalidos')
        input('\nEnter para seguir...')

    elif opcion == 3:
        print('\n--- 3) IF / ELIF / ELSE ---')
        print('Estructura basica: if condicion: ... elif ... else ...')
        print('Demo: mayor de edad')
        e_txt = input('Edad: ').strip()
        if e_txt.isdigit():
            e = int(e_txt)
            if e >= 18:
                print('Mayor de edad')
            else:
                print('Menor de edad')
        else:
            print('Edad invalida')
        input('\nEnter para seguir...')

    elif opcion == 4:
        print('\n--- 4) BUCLE WHILE ---')
        print('while condicion: se repite mientras sea True')
        print('Demo: contar 0..n-1')
        n_txt = input('n: ').strip()
        if n_txt.isdigit():
            n = int(n_txt)
            i = 0
            while i < n:
                print('i =', i)
                i += 1
        else:
            print('n invalido')
        input('\nEnter para seguir...')

    elif opcion == 5:
        print('\n--- 5) MATCH / CASE (Python 3.10+) ---')
        print('Estructura tipo switch. Si tu Python es viejo, usar if/elif.')
        print('Ejemplo:')
        print('  op = int(input("Opcion: "))')
        print('  match op:')
        print('      case 1: print("uno")')
        print('      case 2: print("dos")')
        print('      case _: print("otra")')
        print('Tip: en el parcial pueden pedir case; sino, if/elif.')
        input('\nEnter para seguir...')

    elif opcion == 6:
        print('\n--- 6) LISTAS ---')
        print('Lista: coleccion ordenada. Ej: nombres = ["Ana","Luis"]')
        print('Operaciones: append, len, recorrer con while/for')
        print('\nDemo: cargar nombres y mostrar')
        nombres = []
        c_txt = input('Cuantos nombres?: ').strip()
        if c_txt.isdigit():
            c = int(c_txt)
            if c > 0:
                i = 0
                while i < c:
                    n = input('Nombre: ').strip()
                    if len(n) > 0:
                        nombres.append(n)
                    else:
                        print('No vacio')
                    i += 1
                print('\nLista final:')
                i = 0
                while i < len(nombres):
                    print('-', nombres[i])
                    i += 1
            else:
                print('Cantidad invalida')
        else:
            print('Invalido')
        input('\nEnter para seguir...')

    elif opcion == 7:
        print('\n--- 7) LISTAS PARALELAS ---')
        print('Dos listas sincronizadas por indice. Ej: nombres[i] y edades[i]')
        print('Demo: cargar alumnos y edades, y mostrar')
        alumnos = []
        edades = []
        c_txt = input('Cantidad: ').strip()
        if c_txt.isdigit():
            c = int(c_txt)
            if c > 0:
                i = 0
                while i < c:
                    a = input('Alumno: ').strip()
                    e_txt = input('Edad: ').strip()
                    if len(a) == 0:
                        print('Alumno vacio')
                    elif not e_txt.isdigit():
                        print('Edad invalida')
                    else:
                        alumnos.append(a)
                        edades.append(int(e_txt))
                    i += 1
                print('\nListado:')
                i = 0
                while i < len(alumnos):
                    print(alumnos[i], '-', edades[i])
                    i += 1
            else:
                print('Cantidad invalida')
        else:
            print('Invalido')
        input('\nEnter para seguir...')

    elif opcion == 8:
        print('\n--- 8) VALIDACIONES SIN EXCEPCIONES ---')
        print('Usar .isdigit() para numeros. Chequear vacios para textos.')
        print('Demo: leer entero >= 0')
        dato = input('Ingrese un entero >=0: ').strip()
        if dato.isdigit():
            n = int(dato)
            if n >= 0:
                print('OK, n=', n)
            else:
                print('Debe ser >=0')
        else:
            print('Invalido')
        input('\nEnter para seguir...')

    elif opcion == 9:
        print('\n--- 9) MENU PERSISTENTE (PLANTILLA) ---')
        print('Plantilla tipica: while True + if/elif + opcion salir')
        print('Ejemplo:')
        print('  while True:')
        print('      print("1. A\n2. B\n3. Salir")')
        print('      op = input(": ")')
        print('      if op == "1": ... elif op == "2": ... elif op == "3": break')
        input('\nEnter para seguir...')

    elif opcion == 10:
        print('\n--- 10) CASO PRACTICO: BIBLIOTECA ---')
        print('Listas paralelas: libros[] y ejemplares[]')
        libros = []
        ejemplares = []
        salir_biblio = False
        while not salir_biblio:
            print('\n1. Ingresar titulos')
            print('2. Ingresar ejemplares por titulo')
            print('3. Mostrar catalogo')
            print('4. Consultar disponibilidad')
            print('5. Ver agotados')
            print('6. Agregar titulo')
            print('7. Actualizar ejemplares (prestamo/devolucion)')
            print('8. Volver')
            op2 = input('Opcion: ').strip()
            if not op2.isdigit():
                print('Opcion invalida')
                continue
            o2 = int(op2)
            if o2 == 1:
                cs = input('Cuantos titulos?: ').strip()
                if cs.isdigit():
                    c = int(cs)
                    if c > 0:
                        i = 0
                        while i < c:
                            t = input('Titulo: ').strip()
                            if len(t) == 0:
                                print('Vacio')
                            else:
                                dup = False
                                j = 0
                                while j < len(libros):
                                    if libros[j].lower() == t.lower():
                                        dup = True
                                    j += 1
                                if dup:
                                    print('Ya existe')
                                else:
                                    libros.append(t)
                                    ejemplares.append(0)
                            i += 1
                    else:
                        print('Cantidad invalida')
                else:
                    print('Invalido')
            elif o2 == 2:
                if len(libros) == 0:
                    print('No hay titulos')
                else:
                    i = 0
                    while i < len(libros):
                        ok = False
                        while not ok:
                            s = input('Ejemplares para "' + libros[i] + '": ').strip()
                            if s.isdigit():
                                n = int(s)
                                if n >= 0:
                                    ejemplares[i] = n
                                    ok = True
                                else:
                                    print('No negativo')
                            else:
                                print('Ingrese entero >=0')
                        i += 1
            elif o2 == 3:
                if len(libros) == 0:
                    print('No hay libros')
                else:
                    i = 0
                    while i < len(libros):
                        print(libros[i] + ': ' + str(ejemplares[i]) + ' ejemplares')
                        i += 1
            elif o2 == 4:
                if len(libros) == 0:
                    print('No hay titulos')
                else:
                    b = input('Titulo: ').strip()
                    if len(b) == 0:
                        print('Vacio')
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
                            print('Disponibles:', ejemplares[idx])
            elif o2 == 5:
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
            elif o2 == 6:
                nuevo = input('Titulo nuevo: ').strip()
                if len(nuevo) == 0:
                    print('Vacio')
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
                        s = input('Ejemplares iniciales: ').strip()
                        if s.isdigit():
                            n = int(s)
                            if n < 0:
                                n = 0
                        else:
                            n = 0
                        libros.append(nuevo)
                        ejemplares.append(n)
                        print('Agregado')
            elif o2 == 7:
                if len(libros) == 0:
                    print('No hay titulos')
                else:
                    nombre = input('Titulo: ').strip()
                    if len(nombre) == 0:
                        print('Vacio')
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
                            ts = input('Opcion: ').strip()
                            if ts.isdigit():
                                tipo = int(ts)
                                if tipo == 1 or tipo == 2:
                                    cs = input('Cantidad: ').strip()
                                    if cs.isdigit():
                                        cant = int(cs)
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
            elif o2 == 8:
                salir_biblio = True
            else:
                print('Opcion invalida')
        input('\nEnter para seguir...')

    elif opcion == 11:
        print('\n--- 11) QUIZ RAPIDO (10 PREGUNTAS) ---')
        puntaje = 0
        # P1
        print('1) .isdigit() sirve para:')
        print('   a) comprobar si un string es numerico entero positivo')
        print('   b) convertir texto a entero')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P2
        print('2) En listas paralelas, el indice 2 en titulos y ejemplares apunta a:')
        print('   a) el mismo libro y su stock')
        print('   b) libros distintos')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P3
        print('3) En este curso, para validar numeros evitamos:')
        print('   a) excepciones try/except')
        print('   b) .isdigit()')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P4
        print('4) El menu persistente se logra con:')
        print('   a) while True')
        print('   b) for')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P5
        print('5) match/case requiere:')
        print('   a) Python 3.10+ ') 
        print('   b) Python 2.7')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P6
        print('6) Prestar mas que el stock:')
        print('   a) permitido')
        print('   b) no permitido')
        r = input('Resp: ').strip().lower()
        if r == 'b':
            puntaje += 1
        # P7
        print('7) Para evitar duplicados de titulos usamos:')
        print('   a) comparar lower() en un bucle')
        print('   b) nada')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P8
        print('8) Un titulo vacio:')
        print('   a) se acepta')
        print('   b) no se acepta')
        r = input('Resp: ').strip().lower()
        if r == 'b':
            puntaje += 1
        # P9
        print('9) Para mostrar catalogo:')
        print('   a) recorrer ambas listas con el mismo indice')
        print('   b) recorrer una sola lista')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        # P10
        print('10) if/elif/else sirve para:')
        print('    a) decisiones')
        print('    b) repetir')
        r = input('Resp: ').strip().lower()
        if r == 'a':
            puntaje += 1
        print('\nPuntaje:', puntaje, '/ 10')
        if puntaje == 10:
            print('Excelente!')
        elif puntaje >= 7:
            print('Muy bien!')
        else:
            print('A practicar un poco mas.')
        input('\nEnter para seguir...')

    elif opcion == 12:
        print('Saliendo...')
        salir_total = True
    else:
        print('Opcion invalida')
