import csv
import os
from typing import List, Dict

# ===== Utilidades de entrada/salida =====

def get_csv_path(nombre_archivo: str = "paises.csv") -> str:
    """Devuelve la ruta absoluta del CSV relativa a este archivo (robusta)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, nombre_archivo)


def cargar_datos(archivo: str) -> List[Dict]:
    """
    Lee el archivo CSV y retorna una lista de diccionarios con los datos de países.
    Cada país es un diccionario con: nombre, poblacion, superficie, continente
    """
    paises: List[Dict] = []
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                if not fila:
                    continue
                try:
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                except (KeyError, ValueError):
                    # Salteamos filas mal formateadas
                    continue
                paises.append(pais)
        print(f"\u2713 Se cargaron {len(paises)} países correctamente.\n")
        return paises
    except FileNotFoundError:
        print(f"\u2717 Error: No se encontró el archivo '{archivo}'")
        return []
    except ValueError:
        print("\u2717 Error: El archivo contiene datos con formato incorrecto")
        return []
    except Exception as e:
        print(f"\u2717 Error inesperado: {e}")
        return []
