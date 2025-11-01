"""
Sistema de Gestión de Países
Trabajo Práctico Integrador - Programación 1

Permite realizar operaciones de búsqueda, filtrado, ordenamiento y estadísticas
sobre un conjunto de datos de países almacenados en archivo CSV.
"""

from funciones.funciones import cargar_paises, guardar_paises
from funciones.funciones_operaciones import (
    buscar_por_nombre, filtrar_por_continente, filtrar_por_rango,
    ordenar, estadisticas
)
from funciones.funciones_altas_bajas import agregar_pais, quitar_pais, editar_pais
from funciones.mostrar_lista import mostrar_lista
from funciones.menu import menu
from funciones.utilidades import preguntar_nuevamente, pedir_int, pausar, menu_salida

RUTA = "paises.csv"


def submenu_buscar_nombre(paises):
    """Búsqueda de países por nombre (coincidencia parcial)."""
    while True:
        print("\n--- BUSCAR POR NOMBRE ---")
        texto = input("Texto a buscar (o 'volver' para regresar): ").strip()
        
        if texto.lower() == "volver":
            break
        
        if not texto:
            print("Debe ingresar un texto a buscar.")
            continue
        
        resultados = buscar_por_nombre(paises, texto)
        mostrar_lista(resultados)
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_filtrar_continente(paises):
    """Filtrado de países por continente."""
    while True:
        print("\n--- FILTRAR POR CONTINENTE ---")
        print("Continentes disponibles: América, Europa, Asia, África, Oceanía")
        cont = input("Continente (o 'volver' para regresar): ").strip()
        
        if cont.lower() == "volver":
            break
        
        if not cont:
            print("Debe ingresar un continente.")
            continue
        
        resultados = filtrar_por_continente(paises, cont)
        if len(resultados) == 0:
            print(f"No se encontraron países en el continente '{cont}'.")
        else:
            mostrar_lista(resultados)
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_filtrar_poblacion(paises):
    """Filtrado de países por rango de población."""
    while True:
        print("\n--- FILTRAR POR POBLACIÓN (RANGO) ---")
        volver = input("¿Desea realizar un filtrado? (si/no): ").strip().lower()
        
        if volver == "no":
            break
        elif volver != "si":
            print("Respuesta inválida.")
            continue
        
        print("Dejá vacío un límite si no querés aplicarlo.")
        mn = pedir_int("Población mínima: ", vacio=True)
        mx = pedir_int("Población máxima: ", vacio=True)
        
        if mn is None and mx is None:
            print("Debe especificar al menos un límite (mínimo o máximo).")
            continue
        
        resultados = filtrar_por_rango(paises, "poblacion", mn, mx)
        mostrar_lista(resultados)
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_filtrar_superficie(paises):
    """Filtrado de países por rango de superficie."""
    while True:
        print("\n--- FILTRAR POR SUPERFICIE (RANGO) ---")
        volver = input("¿Desea realizar un filtrado? (si/no): ").strip().lower()
        
        if volver == "no":
            break
        elif volver != "si":
            print("Respuesta inválida.")
            continue
        
        print("Dejá vacío un límite si no querés aplicarlo.")
        mn = pedir_int("Superficie mínima (km²): ", vacio=True)
        mx = pedir_int("Superficie máxima (km²): ", vacio=True)
        
        if mn is None and mx is None:
            print("Debe especificar al menos un límite (mínimo o máximo).")
            continue
        
        resultados = filtrar_por_rango(paises, "superficie", mn, mx)
        mostrar_lista(resultados)
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_ordenar(paises):
    """Ordenamiento de países por nombre, población o superficie."""
    while True:
        print("\n--- ORDENAR PAÍSES ---")
        print("Criterios disponibles: nombre, población, superficie")
        clave = input("Criterio de ordenamiento (o 'volver' para regresar): ").strip().lower()
        
        if clave == "volver":
            break
        
        if clave not in ("nombre", "poblacion", "superficie"):
            print("Criterio inválido. Debe ser: nombre, población o superficie.")
            continue
        
        sentido = input("Orden (asc/desc): ").strip().lower()
        
        if sentido not in ("asc", "desc"):
            print("Orden inválido. Debe ser: asc o desc.")
            continue
        
        desc = (sentido == "desc")
        resultados = ordenar(paises, clave, desc)
        mostrar_lista(resultados)
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_estadisticas(paises):
    """Estadísticas interactivas: permite elegir qué indicador visualizar."""
    while True:
        print("\n--- ESTADÍSTICAS GENERALES ---")

        est = estadisticas(paises)
        if not est:
            print("No hay datos para calcular estadísticas.")
            accion = menu_salida()
            if accion == "submenu":
                continue
            else:
                break

        # Mostrar menú de selección de estadística
        print("¿Qué estadística desea ver?")
        print("  [1] País con mayor población")
        print("  [2] País con menor población")
        print("  [3] Promedios (población y superficie)")
        print("  [4] Cantidad de países por continente")
        print("  [5] Todas las estadísticas")
        print("  [6] Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                print(f"\nPaís con mayor población: {est['mayor']['nombre']} ({est['mayor']['poblacion']:,} habitantes)")
            case "2":
                print(f"\nPaís con menor población: {est['menor']['nombre']} ({est['menor']['poblacion']:,} habitantes)")
            case "3":
                print(f"\nPromedio de población: {est['prom_pobl']:,.2f} habitantes")
                print(f"Promedio de superficie: {est['prom_sup']:,.2f} km²")
            case "4":
                print("\nCantidad de países por continente:")
                for c, n in est["por_cont"].items():
                    print(f"  • {c}: {n} países")
            case "5":
                print(f"\nPaís con mayor población: {est['mayor']['nombre']} ({est['mayor']['poblacion']:,} habitantes)")
                print(f"País con menor población: {est['menor']['nombre']} ({est['menor']['poblacion']:,} habitantes)")
                print(f"Promedio de población: {est['prom_pobl']:,.2f} habitantes")
                print(f"Promedio de superficie: {est['prom_sup']:,.2f} km²")
                print("\nCantidad de países por continente:")
                for c, n in est["por_cont"].items():
                    print(f"  • {c}: {n} países")
            case "6":
                break
            case _:
                print("Opción inválida. Intente de nuevo.")
                continue

        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_agregar_pais(paises):
    """Agregar nuevos países al sistema."""
    while True:
        print("\n--- AGREGAR NUEVO PAÍS ---")
        
        n = input("Nombre del país: ").strip()
        if not n:
            print("El nombre no puede estar vacío.")
            pausar()
            continuar = input("\n¿Desea intentar agregar otro país? (si/no): ").strip().lower()
            if continuar != "si":
                break
            continue
        
        p = pedir_int("Población: ")
        if p is None:
            print("Población inválida.")
            pausar()
            continuar = input("\n¿Desea intentar agregar otro país? (si/no): ").strip().lower()
            if continuar != "si":
                break
            continue
        
        s = pedir_int("Superficie (km²): ")
        if s is None:
            print("Superficie inválida.")
            pausar()
            continuar = input("\n¿Desea intentar agregar otro país? (si/no): ").strip().lower()
            if continuar != "si":
                break
            continue
        
        c = input("Continente: ").strip()
        if not c:
            print("El continente no puede estar vacío.")
            pausar()
            continuar = input("\n¿Desea intentar agregar otro país? (si/no): ").strip().lower()
            if continuar != "si":
                break
            continue
        
        # Preguntar si está reconocido por la ONU
        onu = input("¿El país es reconocido por la ONU? (si/no): ").strip().lower()
        while onu not in ("si", "no"):
            print("Respuesta inválida. Ingrese 'si' o 'no'.")
            onu = input("¿El país es reconocido por la ONU? (si/no): ").strip().lower()
        
        reconocido = (onu == "si")
        
        ok = agregar_pais(paises, n, p, s, c, reconocido)
        if ok:
            print(f"✓ País '{n}' agregado exitosamente.")
        else:
            print(f"✗ No se pudo agregar el país (puede estar duplicado o los datos son inválidos).")
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_editar_pais(paises):
    """Editar datos de un país existente."""
    while True:
        print("\n--- EDITAR PAÍS ---")
        n = input("Nombre exacto del país a editar (o 'volver' para regresar): ").strip()
        
        if n.lower() == "volver":
            break
        
        if not n:
            print("Debe ingresar un nombre.")
            continue
        
        # Buscar el país
        pais = editar_pais(paises, n)
        if not pais:
            print(f"✗ No se encontró el país '{n}'.")
            accion = menu_salida()
            if accion != "submenu":
                break
            continue
        
        # Mostrar datos actuales
        print(f"\nDatos actuales de '{pais['nombre']}':")
        print(f"  Población: {pais['poblacion']:,}")
        print(f"  Superficie: {pais['superficie']:,} km²")
        print(f"  Continente: {pais['continente']}")
        reconocido_str = "Sí" if pais.get('reconocido_onu', True) else "No"
        print(f"  Reconocido por ONU: {reconocido_str}")
        
        # Preguntar qué campo editar
        print("\n¿Qué desea editar?")
        print("  [1] Nombre")
        print("  [2] Población")
        print("  [3] Superficie")
        print("  [4] Continente")
        print("  [5] Reconocido por ONU")
        print("  [6] Cancelar")
        
        opcion = input("Seleccione una opción: ").strip()
        
        match opcion:
            case "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    pais["nombre"] = nuevo_nombre
                    print("✓ Nombre actualizado.")
                else:
                    print("✗ El nombre no puede estar vacío.")
            
            case "2":
                nueva_pob = pedir_int("Nueva población: ")
                if nueva_pob is not None and nueva_pob >= 0:
                    pais["poblacion"] = nueva_pob
                    print("✓ Población actualizada.")
                else:
                    print("✗ Población inválida.")
            
            case "3":
                nueva_sup = pedir_int("Nueva superficie (km²): ")
                if nueva_sup is not None and nueva_sup >= 0:
                    pais["superficie"] = nueva_sup
                    print("✓ Superficie actualizada.")
                else:
                    print("✗ Superficie inválida.")
            
            case "4":
                nuevo_cont = input("Nuevo continente: ").strip()
                if nuevo_cont:
                    pais["continente"] = nuevo_cont
                    print("✓ Continente actualizado.")
                else:
                    print("✗ El continente no puede estar vacío.")
            
            case "5":
                onu = input("¿El país es reconocido por la ONU? (si/no): ").strip().lower()
                while onu not in ("si", "no"):
                    print("Respuesta inválida. Ingrese 'si' o 'no'.")
                    onu = input("¿El país es reconocido por la ONU? (si/no): ").strip().lower()
                
                pais["reconocido_onu"] = (onu == "si")
                print("✓ Estado de reconocimiento ONU actualizado.")
            
            case "6":
                print("Edición cancelada.")
            
            case _:
                print("✗ Opción inválida.")
        
        accion = menu_salida()
        if accion != "submenu":
            break


def submenu_quitar_pais(paises):
    """Eliminar países del sistema."""
    while True:
        print("\n--- ELIMINAR PAÍS ---")
        n = input("Nombre exacto del país a eliminar (o 'volver' para regresar): ").strip()
        
        if n.lower() == "volver":
            break
        
        if not n:
            print("Debe ingresar un nombre.")
            continue
        
        eliminado = quitar_pais(paises, n)
        if eliminado:
            print(f"✓ País '{n}' eliminado exitosamente.")
        else:
            print(f"✗ No se encontró el país '{n}'.")
        
        accion = menu_salida()
        if accion != "submenu":
            break


def main():
    """Función principal: gestiona el menú y las operaciones del sistema."""
    paises = cargar_paises(RUTA)
    print(f"\n╔═══════════════════════════════════════════════╗")
    print(f"║  Sistema de Gestión de Países                 ║")
    print(f"╚═══════════════════════════════════════════════╝")
    print(f"Total de países cargados: {len(paises)}")
    
    while True:
        menu()
        op = input("Seleccione una opción: ").strip()
        
        match op:
            case "1":
                submenu_buscar_nombre(paises)
            
            case "2":
                submenu_filtrar_continente(paises)
            
            case "3":
                submenu_filtrar_poblacion(paises)
            
            case "4":
                submenu_filtrar_superficie(paises)
            
            case "5":
                submenu_ordenar(paises)
            
            case "6":
                submenu_estadisticas(paises)
            
            case "7":
                submenu_agregar_pais(paises)
            
            case "8":
                submenu_editar_pais(paises)
            
            case "9":
                submenu_quitar_pais(paises)
            
            case "0":
                print("\n--- GUARDANDO CAMBIOS ---")
                try:
                    guardar_paises(paises, RUTA)
                    print("✓ Cambios guardados exitosamente.")
                    print("¡Hasta luego!")
                except Exception as e:
                    print(f"✗ Error al guardar: {e}")
                break
            
            case _:
                print("✗ Opción inválida. Por favor, seleccione una opción del 1 al 9 o 0.")
                pausar()


if __name__ == "__main__":
    main()