def _existe_nombre(paises, nombre):
    """
    Verifica si ya existe un país con el nombre dado (función auxiliar).
    
    Args:
        paises: lista de diccionarios con datos de países
        nombre: nombre del país a verificar
    
    Returns:
        True si el país ya existe, False en caso contrario
    """
    n = nombre.strip().lower()
    for p in paises:
        if p["nombre"].lower() == n:
            return True
    return False

def agregar_pais(paises, nombre, poblacion, superficie, continente, reconocido_onu=True):
    """
    Agrega un nuevo país a la lista si no existe duplicado.
    
    Args:
        paises: lista de diccionarios con datos de países
        nombre: nombre del país
        poblacion: población del país
        superficie: superficie en km²
        continente: continente al que pertenece
        reconocido_onu: si el país está reconocido por la ONU (default: True)
    
    Returns:
        True si se agregó exitosamente, False si hubo error o duplicado
    """
    # Verificar si ya existe
    if _existe_nombre(paises, nombre):
        return False
    
    # Intentar crear el nuevo país con validación de tipos
    try:
        # Convertir y redondear superficie para mantener consistencia con el cargador
        nuevo = {
            "nombre": nombre.strip(),
            "poblacion": int(poblacion),
            "superficie": int(round(float(superficie))),
            "continente": continente.strip(),
            "reconocido_onu": reconocido_onu
        }
    except:
        return False
    
    # Validación de datos mínimos
    if not nuevo["nombre"] or nuevo["poblacion"] < 0 or nuevo["superficie"] < 0 or not nuevo["continente"]:
        return False
    
    # Agregar a la lista
    paises.append(nuevo)
    return True

def quitar_pais(paises, nombre):
    """
    Elimina un país de la lista por nombre exacto.
    
    Args:
        paises: lista de diccionarios con datos de países
        nombre: nombre exacto del país a eliminar
    
    Returns:
        True si se eliminó exitosamente, False si no se encontró
    """
    n = nombre.strip().lower()
    antes = len(paises)
    
    # Crear nueva lista sin el país a eliminar
    paises_filtrados = []
    for p in paises:
        if p["nombre"].lower() != n:
            paises_filtrados.append(p)
    
    # Actualizar la lista original
    paises[:] = paises_filtrados
    
    return len(paises) != antes

def editar_pais(paises, nombre):
    """
    Busca un país por nombre exacto para editarlo.
    
    Args:
        paises: lista de diccionarios con datos de países
        nombre: nombre exacto del país a buscar
    
    Returns:
        El país encontrado (diccionario) o None si no existe
    """
    n = nombre.strip().lower()
    for p in paises:
        if p["nombre"].lower() == n:
            return p
    return None