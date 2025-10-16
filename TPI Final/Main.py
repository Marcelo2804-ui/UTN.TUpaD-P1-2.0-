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

# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """
    Función principal del programa
    """
    print("=" * 50)
    print("    SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 50)
    
    # Cargar datos del CSV (usando ruta relativa)
    paises = cargar_datos("paises.csv")
    
    if not paises:
        print("No se pueden continuar sin datos. Saliendo...")
        return
    
    # Aquí irá el menú y las demás funcionalidades
    print("Sistema listo. Aquí implementarás el menú...")

# Ejecutar el programa
if _name_ == "_main_":
    main()