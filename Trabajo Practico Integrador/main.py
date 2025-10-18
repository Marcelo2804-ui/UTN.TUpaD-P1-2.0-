import csv

# ==================== CARGA DE DATOS ====================

def cargar_datos(archivo):
    """
    Lee el archivo CSV y retorna una lista de diccionarios con los datos de países.
    Cada país es un diccionario con: nombre, poblacion, superficie, continente
    """
    paises = []
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                pais = {
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                }
                paises.append(pais)
        print(f"✓ Se cargaron {len(paises)} países correctamente.\n")
        return paises
    except FileNotFoundError:
        print(f"✗ Error: No se encontró el archivo '{archivo}'")
        return []
    except ValueError:
        print("✗ Error: El archivo contiene datos con formato incorrecto")
        return []
    except Exception as e:
        print(f"✗ Error inesperado: {e}")
        return []

# ==================== FUNCIÓN 1: BUSCAR PAÍS ====================

def buscar_pais(paises, nombre_buscar):
    """
    Busca un país por nombre (búsqueda parcial, no distingue mayúsculas/minúsculas)
    """
    resultados = []
    nombre_buscar = nombre_buscar.lower()
    
    for pais in paises:
        if nombre_buscar in pais['nombre'].lower():
            resultados.append(pais)
    
    if resultados:
        print(f"\n{'='*60}")
        print(f"Se encontraron {len(resultados)} resultado(s):")
        print(f"{'='*60}")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"\n✗ No se encontró ningún país con el nombre '{nombre_buscar}'")

def mostrar_pais(pais):
    """
    Muestra los datos de un país de forma legible
    """
    print(f"\n  País: {pais['nombre']}")
    print(f"  Población: {pais['poblacion']:,} habitantes")
    print(f"  Superficie: {pais['superficie']:,} km²")
    print(f"  Continente: {pais['continente']}")
    print(f"  Densidad: {calcular_densidad(pais):.2f} hab/km²")
    print("-" * 60)

def calcular_densidad(pais):
    """
    Calcula la densidad poblacional de un país
    """
    if pais['superficie'] > 0:
        return pais['poblacion'] / pais['superficie']
    return 0

# ==================== FUNCIÓN 2: FILTRAR POR CONTINENTE ====================

def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente
    """
    resultados = [p for p in paises if p['continente'].lower() == continente.lower()]
    
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países de {continente}: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}")
    else:
        print(f"\n✗ No se encontraron países en el continente '{continente}'")
    
    return resultados

# ==================== FUNCIÓN 3: FILTRAR POR POBLACIÓN ====================

def filtrar_por_poblacion(paises, min_pob, max_pob):
    """
    Filtra países por rango de población
    """
    resultados = [p for p in paises if min_pob <= p['poblacion'] <= max_pob]
    
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países con población entre {min_pob:,} y {max_pob:,}: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}: {pais['poblacion']:,} habitantes")
    else:
        print(f"\n✗ No se encontraron países en ese rango de población")
    
    return resultados

# ==================== FUNCIÓN 4: FILTRAR POR SUPERFICIE ====================

def filtrar_por_superficie(paises, min_sup, max_sup):
    """
    Filtra países por rango de superficie
    """
    resultados = [p for p in paises if min_sup <= p['superficie'] <= max_sup]
    
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países con superficie entre {min_sup:,} y {max_sup:,} km²: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}: {pais['superficie']:,} km²")
    else:
        print(f"\n✗ No se encontraron países en ese rango de superficie")
    
    return resultados

# ==================== FUNCIÓN 5: ORDENAR PAÍSES ====================

def ordenar_paises(paises, criterio, descendente=False):
    """
    Ordena la lista de países según el criterio especificado
    criterio: 'nombre', 'poblacion', 'superficie', 'densidad'
    """
    if criterio == 'nombre':
        ordenados = sorted(paises, key=lambda p: p['nombre'], reverse=descendente)
    elif criterio == 'poblacion':
        ordenados = sorted(paises, key=lambda p: p['poblacion'], reverse=descendente)
    elif criterio == 'superficie':
        ordenados = sorted(paises, key=lambda p: p['superficie'], reverse=descendente)
    elif criterio == 'densidad':
        ordenados = sorted(paises, key=lambda p: calcular_densidad(p), reverse=descendente)
    else:
        print(f"✗ Criterio '{criterio}' no válido")
        return paises
    
    return ordenados

def mostrar_ordenados(paises, criterio, descendente):
    """
    Muestra los países ordenados
    """
    ordenados = ordenar_paises(paises, criterio, descendente)
    orden_texto = "descendente" if descendente else "ascendente"
    
    print(f"\n{'='*60}")
    print(f"Países ordenados por {criterio} ({orden_texto}):")
    print(f"{'='*60}")
    
    for i, pais in enumerate(ordenados[:20], 1):  # Mostrar solo los primeros 20
        if criterio == 'nombre':
            print(f"  {i}. {pais['nombre']}")
        elif criterio == 'poblacion':
            print(f"  {i}. {pais['nombre']}: {pais['poblacion']:,} habitantes")
        elif criterio == 'superficie':
            print(f"  {i}. {pais['nombre']}: {pais['superficie']:,} km²")
        elif criterio == 'densidad':
            print(f"  {i}. {pais['nombre']}: {calcular_densidad(pais):.2f} hab/km²")
    
    if len(ordenados) > 20:
        print(f"\n  ... y {len(ordenados) - 20} países más")

# ==================== FUNCIÓN 6: ESTADÍSTICAS ====================

def mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales de todos los países
    """
    if not paises:
        print("✗ No hay datos para mostrar estadísticas")
        return
    
    # Calcular estadísticas de población
    poblaciones = [p['poblacion'] for p in paises]
    total_poblacion = sum(poblaciones)
    promedio_poblacion = total_poblacion / len(paises)
    max_poblacion = max(paises, key=lambda p: p['poblacion'])
    min_poblacion = min(paises, key=lambda p: p['poblacion'])
    
    # Calcular estadísticas de superficie
    superficies = [p['superficie'] for p in paises]
    total_superficie = sum(superficies)
    promedio_superficie = total_superficie / len(paises)
    max_superficie = max(paises, key=lambda p: p['superficie'])
    min_superficie = min(paises, key=lambda p: p['superficie'])
    
    # Calcular estadísticas por continente
    continentes = {}
    for pais in paises:
        cont = pais['continente']
        if cont not in continentes:
            continentes[cont] = 0
        continentes[cont] += 1
    
    # Mostrar resultados
    print(f"\n{'='*60}")
    print("ESTADÍSTICAS GENERALES")
    print(f"{'='*60}")
    print(f"\nTotal de países: {len(paises)}")
    
    print(f"\n--- POBLACIÓN ---")
    print(f"  Total mundial: {total_poblacion:,} habitantes")
    print(f"  Promedio: {promedio_poblacion:,.0f} habitantes")
    print(f"  País más poblado: {max_poblacion['nombre']} ({max_poblacion['poblacion']:,})")
    print(f"  País menos poblado: {min_poblacion['nombre']} ({min_poblacion['poblacion']:,})")
    
    print(f"\n--- SUPERFICIE ---")
    print(f"  Total: {total_superficie:,} km²")
    print(f"  Promedio: {promedio_superficie:,.0f} km²")
    print(f"  País más grande: {max_superficie['nombre']} ({max_superficie['superficie']:,} km²)")
    print(f"  País más pequeño: {min_superficie['nombre']} ({min_superficie['superficie']:,} km²)")
    
    print(f"\n--- PAÍSES POR CONTINENTE ---")
    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente}: {cantidad} países")
    
    print(f"\n{'='*60}")

# ==================== FUNCIÓN 7: LISTAR CONTINENTES ====================

def listar_continentes(paises):
    """
    Lista todos los continentes disponibles
    """
    continentes = set(p['continente'] for p in paises)
    print(f"\n{'='*60}")
    print("CONTINENTES DISPONIBLES:")
    print(f"{'='*60}")
    for continente in sorted(continentes):
        cantidad = sum(1 for p in paises if p['continente'] == continente)
        print(f"  - {continente} ({cantidad} países)")

# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    """
    Muestra el menú principal
    """
    print(f"\n{'='*60}")
    print("MENÚ PRINCIPAL")
    print(f"{'='*60}")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas generales")
    print("7. Listar continentes disponibles")
    print("0. Salir")
    print(f"{'='*60}")

def menu_ordenar():
    """
    Submenú para ordenar países
    """
    print("\n¿Por qué criterio desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    print("4. Densidad poblacional")
    criterio_opc = input("Seleccione opción: ").strip()
    
    criterios = {'1': 'nombre', '2': 'poblacion', '3': 'superficie', '4': 'densidad'}
    criterio = criterios.get(criterio_opc)
    
    if not criterio:
        print("✗ Opción no válida")
        return None, None
    
    print("\n¿Orden ascendente o descendente?")
    print("1. Ascendente")
    print("2. Descendente")
    orden_opc = input("Seleccione opción: ").strip()
    
    descendente = (orden_opc == '2')
    
    return criterio, descendente

# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """
    Función principal del programa
    """
    print("=" * 60)
    print("    SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 60)
    
    # Cargar datos del CSV
    paises = cargar_datos("paises.csv")
    
    # Verificar que se cargaron los datos
    if not paises:
        print("No se pueden continuar sin datos. Saliendo...")
        return
    
    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            # Buscar país por nombre
            nombre = input("\nIngrese el nombre del país a buscar: ").strip()
            if nombre:
                buscar_pais(paises, nombre)
            else:
                print("✗ Debe ingresar un nombre")
        
        elif opcion == '2':
            # Filtrar por continente
            listar_continentes(paises)
            continente = input("\nIngrese el nombre del continente: ").strip()
            if continente:
                filtrar_por_continente(paises, continente)
            else:
                print("✗ Debe ingresar un continente")
        
        elif opcion == '3':
            # Filtrar por población
            try:
                min_pob = int(input("\nIngrese población mínima: ").strip())
                max_pob = int(input("Ingrese población máxima: ").strip())
                if min_pob <= max_pob:
                    filtrar_por_poblacion(paises, min_pob, max_pob)
                else:
                    print("✗ El mínimo debe ser menor o igual al máximo")
            except ValueError:
                print("✗ Debe ingresar números válidos")
        
        elif opcion == '4':
            # Filtrar por superficie
            try:
                min_sup = int(input("\nIngrese superficie mínima (km²): ").strip())
                max_sup = int(input("Ingrese superficie máxima (km²): ").strip())
                if min_sup <= max_sup:
                    filtrar_por_superficie(paises, min_sup, max_sup)
                else:
                    print("✗ El mínimo debe ser menor o igual al máximo")
            except ValueError:
                print("✗ Debe ingresar números válidos")
        
        elif opcion == '5':
            # Ordenar países
            criterio, descendente = menu_ordenar()
            if criterio:
                mostrar_ordenados(paises, criterio, descendente)
        
        elif opcion == '6':
            # Mostrar estadísticas
            mostrar_estadisticas(paises)
        
        elif opcion == '7':
            # Listar continentes
            listar_continentes(paises)
        
        elif opcion == '0':
            # Salir
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        
        else:
            print("\n✗ Opción no válida. Por favor, seleccione una opción del menú.")
        
        # Pausa para que el usuario vea los resultados
        input("\nPresione ENTER para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()