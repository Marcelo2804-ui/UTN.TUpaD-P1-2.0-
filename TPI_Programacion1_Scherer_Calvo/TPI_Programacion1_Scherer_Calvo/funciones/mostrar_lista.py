"""
Módulo para visualización de listados de países.
Proporciona funcionalidad de paginación para mostrar resultados de forma organizada.
"""

def mostrar_lista(paises, por_pagina=10):
    """
    Muestra una lista de países con sistema de paginación.
    
    Args:
        paises: lista de diccionarios con datos de países
        por_pagina: cantidad de países a mostrar por página (default: 10)
    """
    # Validar que haya resultados
    if not paises:
        print("Sin resultados ")
        return
    
    total = len(paises)
    # Calcular total de páginas (redondeo hacia arriba)
    total_paginas = (total + por_pagina - 1) // por_pagina
    pagina_actual = 1
    
    # Bucle de navegación entre páginas
    while True:
        # Calcular índices de inicio y fin para la página actual
        inicio = (pagina_actual - 1) * por_pagina
        fin = min(inicio + por_pagina, total)
        
        # Encabezado de página
        print(f"\n╔════════════════════════════════════════════════════════════════════════════╗")
        print(f"║  Resultados: {total} países - Página {pagina_actual} de {total_paginas}")
        print(f"╚════════════════════════════════════════════════════════════════════════════╝")
        
        # Mostrar países de la página actual
        for i in range(inicio, fin):
            num_global = i + 1
            p = paises[i]
            # Formatear números con separadores de miles
            poblacion_fmt = f"{p['poblacion']:,}".replace(",", ".")
            superficie_fmt = f"{p['superficie']:,}".replace(",", ".")
            # Indicador de reconocimiento por la ONU
            onu_tag = "" if p.get('reconocido_onu', True) else " [No reconocido por ONU]"
            print(f"{num_global:3d}. {p['nombre']:30s} | Pob: {poblacion_fmt:>15s} | Sup: {superficie_fmt:>12s} km² | {p['continente']}{onu_tag}")
        
        # Opciones de navegación (solo si hay múltiples páginas)
        if total_paginas > 1:
            print(f"\n┌────────────────────────────────────────────────────────────────────────────┐")
            print(f"│ Navegación:                                                                │")
            print(f"│   [S]iguiente página | [A]nterior página | [Número] para ir a una página  │")
            print(f"│   [V]olver (para salir de la visualización)                               │")
            print(f"└────────────────────────────────────────────────────────────────────────────┘")
            opcion = input("Opción: ").strip().lower()
            
            # Procesar opción del usuario
            if opcion == "v" or opcion == "volver" or opcion == "":
                # Volver: salir de la visualización
                break
            elif opcion == "s" or opcion == "siguiente":
                # Siguiente página
                if pagina_actual < total_paginas:
                    pagina_actual += 1
                else:
                    print("Ya estás en la última página.")
            elif opcion == "a" or opcion == "anterior":
                # Página anterior
                if pagina_actual > 1:
                    pagina_actual -= 1
                else:
                    print("Ya estás en la primera página.")
            elif opcion.isdigit():
                # Ir a página específica
                num_pag = int(opcion)
                if 1 <= num_pag <= total_paginas:
                    pagina_actual = num_pag
                else:
                    print(f"Página inválida. Debe estar entre 1 y {total_paginas}.")
            else:
                print("Opción no válida.")
        else:
            # Solo una página: presionar Enter para continuar
            input("\n[Presione ENTER para continuar]")
            break