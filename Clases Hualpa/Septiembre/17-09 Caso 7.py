
alumnos = []
asistencias = []
opcion = 0

# MENU

while opcion != 7:
    print('Si desea salir, coloque "Salir"')
    print('\n1. Agregar un estudiante: ')
    print('2. Agregar una lista de estudiantes: ')
    print('3. Mostrar listado con asistencias: ')
    print('4. Consultar asistencias por estudiante: ')
    print('5. Listar estudiantes con asistencia 0: ')
    print('6. Agregar asistencia por alumno: ')
    print('7. Salir: ')

    try:
        opcion = int(input('\nElige una opción: '))
    except ValueError:
        print("Opción inválida. Ingresa un número.")
        continue

    if opcion == 1:
        alumno = input('Ingrese el nombre del alumno a agregar: ').lower()
        if alumno.isalpha() or alumno.strip() != '':
            alumnos.append(alumno)
            asistencias.append(0)
        else:
            print('Valor inválido.')

    elif opcion == 2:
        cant = input('Ingrese la cantidad de estudiantes a agregar: ')
        if cant.isdigit():
            cant = int(cant)
            for i in range(cant):
                alumno = input('Ingrese el nombre del estudiante: ').lower()
                alumnos.append(alumno)
                asistencias.append(0)
        else:
            print('Valor inválido.')
        
    elif opcion == 3:
        if alumnos:
            for i in range(len(alumnos)):
                print(f'{alumnos[i]}: {asistencias[i]} asistencias') 
                break # optimiza codigo, si encuentra el alumno, termina el if.
        else:
            print('Lista alumnos vacios.')

    elif opcion == 4:
        alumno_buscado =  input('Ingrese el alumno para consultar su asistencia: ')
        if alumnos:
            for i in range(len(alumnos)):
                if alumnos[i] == alumno_buscado.lower():
                    print(f'{alumnos[i]}: {asistencias[i]} asistencias')
                    break # optimiza codigo, si encuentra el alumno, termina el if.
                else:
                    print('Alumno no encontrado.')
        else:
            print('Lista alumnos vacios.')
            
    elif opcion == 5:
        inasistencia = []  # lista vacía donde guardamos los alumnos con 0 asistencia
        for i in range(len(alumnos)):   
            if asistencias[i] == 0:     # si ese alumno tiene 0 asistencia
                inasistencia.append(alumnos[i])  # lo agregamos a la lista

        if inasistencia:  # si la lista no está vacía
            print('Alumnos con 0 asistencias:')
            for alumno in inasistencia:
                print(f'- {alumno}')
        else:
            print('No hay alumnos con 0 asistencias.')

    elif opcion == 6:  
        alumno_buscado = input('Ingrese el nombre del alumno para agregar asistencia: ').lower()
        if alumnos:
            for i in range(len(alumnos)):
                if alumnos[i] == alumno_buscado:
                    asistencias[i] += 1
                    print(f'Se ha agregado una asistencia a {alumnos[i]}. Total asistencias: {asistencias[i]}')
                    break  # optimiza codigo, si encuentra el alumno, termina el if.
            else:
                print('Alumno no encontrado.')
        else:
            print('Lista alumnos vacios.')

    elif opcion == 7:
        print('Saliendo del programa...')
        
    else:
        print('Opción inválida. Por favor, elige una opción del 1 al 7.')
    print()  # mejor legibilidad
