from typing import List, Dict, Tuple

# ===== Lógica de negocio y presentación =====

Pais = Dict[str, object]


def calcular_densidad(pais: Pais) -> float:
    """Calcula la densidad poblacional de un país."""
    superficie = pais.get('superficie', 0) or 0
    poblacion = pais.get('poblacion', 0) or 0
    try:
        superficie = int(superficie)
        poblacion = int(poblacion)
        return poblacion / superficie if superficie > 0 else 0.0
    except (TypeError, ValueError):
        return 0.0


def mostrar_pais(pais: Pais) -> None:
    """Muestra los datos de un país de forma legible."""
    print(f"\n  País: {pais['nombre']}")
    print(f"  Población: {int(pais['poblacion']):,} habitantes")
    print(f"  Superficie: {int(pais['superficie']):,} km²")
    print(f"  Continente: {pais['continente']}")
    print(f"  Densidad: {calcular_densidad(pais):.2f} hab/km²")
    print("-" * 60)


def buscar_pais(paises: List[Pais], nombre_buscar: str) -> List[Pais]:
    """Busca un país por nombre (parcial, case-insensitive)."""
    nombre_buscar = (nombre_buscar or '').lower().strip()
    resultados = [p for p in paises if nombre_buscar in str(p.get('nombre', '')).lower()]

    if resultados:
        print(f"\n{'='*60}")
        print(f"Se encontraron {len(resultados)} resultado(s):")
        print(f"{'='*60}")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"\n\u2717 No se encontró ningún país con el nombre '{nombre_buscar}'")
    return resultados


def filtrar_por_continente(paises: List[Pais], continente: str) -> List[Pais]:
    """Filtra países por continente."""
    resultados = [p for p in paises if str(p.get('continente', '')).lower() == (continente or '').lower().strip()]
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países de {continente}: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}")
    else:
        print(f"\n\u2717 No se encontraron países en el continente '{continente}'")
    return resultados


def filtrar_por_poblacion(paises: List[Pais], min_pob: int, max_pob: int) -> List[Pais]:
    """Filtra países por rango de población."""
    resultados = [p for p in paises if int(p['poblacion']) >= min_pob and int(p['poblacion']) <= max_pob]
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países con población entre {min_pob:,} y {max_pob:,}: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}: {int(pais['poblacion']):,} habitantes")
    else:
        print(f"\n\u2717 No se encontraron países en ese rango de población")
    return resultados


def filtrar_por_superficie(paises: List[Pais], min_sup: int, max_sup: int) -> List[Pais]:
    """Filtra países por rango de superficie."""
    resultados = [p for p in paises if int(p['superficie']) >= min_sup and int(p['superficie']) <= max_sup]
    if resultados:
        print(f"\n{'='*60}")
        print(f"Países con superficie entre {min_sup:,} y {max_sup:,} km²: {len(resultados)} encontrados")
        print(f"{'='*60}")
        for pais in resultados:
            print(f"  - {pais['nombre']}: {int(pais['superficie']):,} km²")
    else:
        print(f"\n\u2717 No se encontraron países en ese rango de superficie")
    return resultados


def ordenar_paises(paises: List[Pais], criterio: str, descendente: bool = False) -> List[Pais]:
    """Ordena la lista de países según criterio: 'nombre', 'poblacion', 'superficie', 'densidad'."""
    if criterio == 'nombre':
        clave = lambda p: str(p.get('nombre', ''))
    elif criterio == 'poblacion':
        clave = lambda p: int(p.get('poblacion', 0) or 0)
    elif criterio == 'superficie':
        clave = lambda p: int(p.get('superficie', 0) or 0)
    elif criterio == 'densidad':
        clave = lambda p: calcular_densidad(p)
    else:
        print(f"\u2717 Criterio '{criterio}' no válido")
        return paises
    return sorted(paises, key=clave, reverse=descendente)


def mostrar_ordenados(paises: List[Pais], criterio: str, descendente: bool) -> None:
    """Muestra los países ordenados (máx 20)."""
    ordenados = ordenar_paises(paises, criterio, descendente)
    orden_texto = "descendente" if descendente else "ascendente"

    print(f"\n{'='*60}")
    print(f"Países ordenados por {criterio} ({orden_texto}):")
    print(f"{'='*60}")

    for i, pais in enumerate(ordenados[:20], 1):
        if criterio == 'nombre':
            print(f"  {i}. {pais['nombre']}")
        elif criterio == 'poblacion':
            print(f"  {i}. {pais['nombre']}: {int(pais['poblacion']):,} habitantes")
        elif criterio == 'superficie':
            print(f"  {i}. {pais['nombre']}: {int(pais['superficie']):,} km²")
        elif criterio == 'densidad':
            print(f"  {i}. {pais['nombre']}: {calcular_densidad(pais):.2f} hab/km²")

    if len(ordenados) > 20:
        print(f"\n  ... y {len(ordenados) - 20} países más")


def mostrar_estadisticas(paises: List[Pais]) -> None:
    """Muestra estadísticas generales de todos los países."""
    if not paises:
        print("\u2717 No hay datos para mostrar estadísticas")
        return

    poblaciones = [int(p['poblacion']) for p in paises]
    superficies = [int(p['superficie']) for p in paises]

    total_poblacion = sum(poblaciones)
    promedio_poblacion = total_poblacion / len(paises)
    max_poblacion = max(paises, key=lambda p: int(p['poblacion']))
    min_poblacion = min(paises, key=lambda p: int(p['poblacion']))

    total_superficie = sum(superficies)
    promedio_superficie = total_superficie / len(paises)
    max_superficie = max(paises, key=lambda p: int(p['superficie']))
    min_superficie = min(paises, key=lambda p: int(p['superficie']))

    continentes: Dict[str, int] = {}
    for pais in paises:
        cont = str(pais['continente'])
        continentes[cont] = continentes.get(cont, 0) + 1

    print(f"\n{'='*60}")
    print("ESTADÍSTICAS GENERALES")
    print(f"{'='*60}")
    print(f"\nTotal de países: {len(paises)}")

    print(f"\n--- POBLACIÓN ---")
    print(f"  Total mundial: {total_poblacion:,} habitantes")
    print(f"  Promedio: {promedio_poblacion:,.0f} habitantes")
    print(f"  País más poblado: {max_poblacion['nombre']} ({int(max_poblacion['poblacion']):,})")
    print(f"  País menos poblado: {min_poblacion['nombre']} ({int(min_poblacion['poblacion']):,})")

    print(f"\n--- SUPERFICIE ---")
    print(f"  Total: {total_superficie:,} km²")
    print(f"  Promedio: {promedio_superficie:,.0f} km²")
    print(f"  País más grande: {max_superficie['nombre']} ({int(max_superficie['superficie']):,} km²)")
    print(f"  País más pequeño: {min_superficie['nombre']} ({int(min_superficie['superficie']):,} km²)")

    print(f"\n--- PAÍSES POR CONTINENTE ---")
    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente}: {cantidad} países")

    print(f"\n{'='*60}")


def listar_continentes(paises: List[Pais]) -> None:
    """Lista todos los continentes disponibles."""
    continentes = set(p['continente'] for p in paises)
    print(f"\n{'='*60}")
    print("CONTINENTES DISPONIBLES:")
    print(f"{'='*60}")
    for continente in sorted(continentes):
        cantidad = sum(1 for p in paises if p['continente'] == continente)
        print(f"  - {continente} ({cantidad} países)")


def mostrar_menu() -> None:
    """Muestra el menú principal."""
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


def menu_ordenar() -> Tuple[str, bool]:
    """Submenú para ordenar países."""
    print("\n¿Por qué criterio desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    print("4. Densidad poblacional")
    criterio_opc = input("Seleccione opción: ").strip()

    criterios = {'1': 'nombre', '2': 'poblacion', '3': 'superficie', '4': 'densidad'}
    criterio = criterios.get(criterio_opc)

    if not criterio:
        print("\u2717 Opción no válida")
        return None, None  # type: ignore

    print("\n¿Orden ascendente o descendente?")
    print("1. Ascendente")
    print("2. Descendente")
    orden_opc = input("Seleccione opción: ").strip()

    descendente = (orden_opc == '2')

    return criterio, descendente
