platos = ["Milanesa con puré", "Ravioles con salsa", "Ensalada César"]
porciones = [10, 15, 20]

while True:
    
    #Menu
    print('Menu: ')
    print('1. Ingresar lista de platos')
    print('2. Ingresar porciones disponibles')
    print('3. Mostrar platos con porciones')
    print('4. Consultar porciones')
    print('5. Listar agotados')
    print('6. Agregar plato')
    print('7. Vender/Devolver porcion')
    print('8. Ver platos con porciones disponibles')
    print('9. Salir')
    
    opcion = input('Ingrese una opcion: ')
    
    match opcion:
        case '1':
            
            cant = input('¿Cuantos platos desea ingresar?')
            
            if not cant.isdigit():
                print('ERROR. Tenes que ingresar un número.')
                continue
            
            cant = int(cant)
            
            for i in range(cant):
                
                while True:
                    plato = input(f"Ingrese el plato {i+1}: ").strip().capitalize()
                    
                    if(plato in platos):
                        print('Este plato ya existe en el menu.')
                        continue
                    else:
                        platos.append(plato)
                        porciones.append(0)
                        print('Plato agregado al menu.')
                        break
            
        case '2':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            for i in range(len(platos)):
                
                while True:
                    porcion = input(f'Ingrese la cantidad de porciones para el plato {platos[i]}: ')
                    
                    if not porcion.isdigit():
                        print('Debe ingresar un número.')
                        continue
                    
                    porcion = int(porcion)
                    
                    porciones[i] = porcion
                    break                   
                
        case '3':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            for i in range(len(platos)):
                print(f'{platos[i]}: {porciones[i]} porciones.')
            
        case '4':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            plato = input('Ingrese el nombre del plato: ').strip().capitalize()
            
            if plato in platos:
                ind = platos.index(plato)
                print(f'Este plato tiene {porciones[ind]} porciones.')
            else:
                print('Este plato no está en el menú.')
            
        case '5':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            for i in range(len(platos)):
                if(porciones[i] == 0):
                    print(f' - {platos[i]}')
            
        case '6':
            while True:
                plato = input(f"Ingrese el nombre del plato: ").strip().capitalize()
                
                if(plato in platos):
                    print('Este plato ya existe en el menu.')
                    continue
                else:
                    platos.append(plato)
                    print('Plato agregado al menu.')
                    break
            
            while True:
                porcion = input(f'Ingrese la cantidad de porciones para el plato {plato}: ')
                
                if not porcion.isdigit():
                    print('Debe ingresar un número.')
                    continue
                
                porcion = int(porcion)
                
                porciones.append(porcion)
                break
            
        case '7':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            plato = input('Ingrese el nombre del plato: ').strip().capitalize()
            
            if(plato in platos):
                ind = platos.index(plato)
                
                opc = input('Ingrese v para vender y d para devolver: ').lower()
                
                if(opc == 'v'):
                    if(porciones[i] == 0):
                        print('No hay porciones disponibles.')
                        continue
                    porciones[i] -= 1
                    print('Porcion vendida.')
                elif(opc == 'd'):
                    porciones[i] += 1
                    print('Porcion devuelta.')
                else:
                    print('Ingresó una opción inválida.')
            
        case '8':
            if not platos:
                print('No hay platos disponibles.')
                continue
            
            for i in range(len(platos)):
                if(porciones[i] != 0):
                    print(f' - {platos[i]}')
            
        case '9':
            print('Hasta luego.')
            break
        case _:
            print('Opción inválida. Ingrese nuevamente.')


