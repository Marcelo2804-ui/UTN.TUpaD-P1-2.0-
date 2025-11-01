"""
Módulo para manejo de archivos CSV de países.
Contiene funciones para cargar y guardar datos de países desde/hacia archivos CSV.
"""

import csv

# Constante: campos esperados en el archivo CSV
CAMPOS = ["nombre", "poblacion", "superficie", "continente", "reconocido_onu"]


def _limpiar_fila_cruda(fila_dict):
    """
    Limpia una fila del CSV eliminando espacios y normalizando claves (función auxiliar).
    
    Args:
        fila_dict: diccionario con datos crudos de una fila del CSV
    
    Returns:
        Diccionario con claves normalizadas (minúsculas, sin espacios)
    """
    limpio = {}
    for k, v in fila_dict.items():
        # Normalizar clave: puede venir None si el CSV tiene columnas extras
        if k is None:
            continue
        kk = k.strip().lower()
        # Normalizar valor: convertir None a cadena vacía, y limpiar strings
        if v is None:
            vv = ""
        elif isinstance(v, str):
            vv = v.strip()
        else:
            vv = v
        limpio[kk] = vv
    return limpio


def _tipar_y_validar(f):
    """
    Convierte tipos de datos y valida valores mínimos (función auxiliar).
    
    Args:
        f: diccionario con datos de un país
    
    Returns:
        Diccionario validado con tipos correctos o None si hay error
    """
    try:
        # Extraer y limpiar campos (proteger contra None)
        nombre = (f.get("nombre") or "").strip()
        poblacion = int(float(f.get("poblacion") or 0))

        # Aceptamos números con decimales para superficie, pero los redondeamos
        superficie_raw = f.get("superficie")
        if superficie_raw is None or superficie_raw == "":
            superficie = 0
        else:
            try:
                superficie = int(round(float(superficie_raw)))
            except:
                return None

        continente = (f.get("continente") or "").strip()

        # Campo opcional: reconocido por la ONU. Si está vacío, asumimos True
        reconocido_raw = f.get("reconocido_onu")
        if reconocido_raw is None or (isinstance(reconocido_raw, str) and reconocido_raw.strip() == ""):
            reconocido = True
        else:
            vr = str(reconocido_raw).strip().lower()
            reconocido = not (vr in ("no", "false", "0", "n", "f"))

        # Validar que los campos no estén vacíos y sean válidos
        if not nombre or poblacion < 0 or superficie < 0 or not continente:
            return None

        # Retornar diccionario validado
        return {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente,
            "reconocido_onu": reconocido
        }
    except:
        # Si hay error en la conversión, retornar None
        return None


def cargar_paises(ruta="paises.csv"):
    """
    Carga datos de países desde un archivo CSV.
    Si el archivo no existe, lo crea con los encabezados.
    
    Args:
        ruta: ruta del archivo CSV (default: "paises.csv")
    
    Returns:
        Lista de diccionarios con datos de países válidos
    """
    paises = []
    try:
        # Abrir archivo en modo lectura con codificación UTF-8
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Procesar cada fila del CSV
            for fila in reader:
                # Limpiar y normalizar la fila
                fila = _limpiar_fila_cruda(fila)
                # Validar y tipar los datos
                ok = _tipar_y_validar(fila)
                # Solo agregar si la validación fue exitosa
                if ok is not None:
                    paises.append(ok)
    except FileNotFoundError:
        # Si el archivo no existe, crearlo con los encabezados
        print(f"Advertencia: archivo '{ruta}' no encontrado. Creando archivo nuevo...")
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=CAMPOS)
                writer.writeheader()
            print(f"✓ Archivo '{ruta}' creado exitosamente. Se iniciará con lista vacía.")
        except Exception as e:
            print(f"✗ Error al crear el archivo: {e}")
        return []
    except Exception as e:
        # Capturar otros errores
        print(f"Error al cargar el archivo: {e}")
        return []
    
    return paises


def guardar_paises(paises, ruta="paises.csv"):
    """
    Guarda la lista de países en un archivo CSV.
    
    Args:
        paises: lista de diccionarios con datos de países
        ruta: ruta del archivo CSV (default: "paises.csv")
    
    Returns:
        True si se guardó exitosamente, False si hubo error
    """
    try:
        # Abrir archivo en modo escritura con codificación UTF-8
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            # Crear escritor CSV con los campos definidos
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            # Escribir encabezado
            writer.writeheader()
            # Escribir todas las filas asegurando el formato del campo 'reconocido_onu'
            for p in paises:
                fila = p.copy()
                # Convertir valor booleano a 'si'/'no' para mejor legibilidad
                fila["reconocido_onu"] = "si" if fila.get("reconocido_onu", True) else "no"
                writer.writerow(fila)
        return True
    except Exception as e:
        # Capturar errores de escritura
        print(f"Error al guardar el archivo: {e}")
        return False