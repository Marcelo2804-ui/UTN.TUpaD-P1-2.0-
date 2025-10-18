from io_utils import get_csv_path, cargar_datos
from operaciones import (
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    mostrar_ordenados,
    mostrar_estadisticas,
    listar_continentes,
    mostrar_menu,
    menu_ordenar,
)
from validaciones import pedir_entero, pedir_texto

# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """
    Función principal del programa
    """
    print("=" * 60)
    print("    SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 60)
    
    # Cargar datos del CSV (ruta robusta relativa a este archivo)
    csv_path = get_csv_path("paises.csv")
    print(f"Cargando datos desde: {csv_path}")
    paises = cargar_datos(csv_path)
    
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
            nombre = pedir_texto("\nIngrese el nombre del país a buscar: ")
            buscar_pais(paises, nombre)
        
        elif opcion == '2':
            # Filtrar por continente
            listar_continentes(paises)
            continente = pedir_texto("\nIngrese el nombre del continente: ")
            filtrar_por_continente(paises, continente)
        
        elif opcion == '3':
            # Filtrar por población
            while True:
                min_pob = pedir_entero("\nIngrese población mínima: ", minimo=0)
                max_pob = pedir_entero("Ingrese población máxima: ", minimo=0)
                if min_pob <= max_pob:
                    filtrar_por_poblacion(paises, min_pob, max_pob)
                    break
                print("✗ El mínimo debe ser menor o igual al máximo")
        
        elif opcion == '4':
            # Filtrar por superficie
            while True:
                min_sup = pedir_entero("\nIngrese superficie mínima (km²): ", minimo=0)
                max_sup = pedir_entero("Ingrese superficie máxima (km²): ", minimo=0)
                if min_sup <= max_sup:
                    filtrar_por_superficie(paises, min_sup, max_sup)
                    break
                print("✗ El mínimo debe ser menor o igual al máximo")
        
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