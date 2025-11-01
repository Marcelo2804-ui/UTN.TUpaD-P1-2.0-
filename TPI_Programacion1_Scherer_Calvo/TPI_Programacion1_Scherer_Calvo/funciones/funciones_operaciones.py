def normalizar_texto(texto):
    """
    Elimina acentos y convierte a minúsculas para búsqueda.
    
    Args:
        texto: cadena de texto a normalizar
    
    Returns:
        Texto normalizado sin acentos y en minúsculas
    """
    import unicodedata
    # Normaliza y elimina acentos
    texto_nfd = unicodedata.normalize('NFD', texto)
    # Eliminar caracteres de marca de acento
    caracteres_sin_acento = []
    for c in texto_nfd:
        if unicodedata.category(c) != 'Mn':
            caracteres_sin_acento.append(c)
    texto_sin_acentos = ''.join(caracteres_sin_acento)
    return texto_sin_acentos.lower()

def buscar_por_nombre(paises, texto):
    """
    Busca países cuyo nombre contenga el texto especificado (búsqueda parcial).
    
    Args:
        paises: lista de diccionarios con datos de países
        texto: texto a buscar en los nombres
    
    Returns:
        Lista de países que coinciden con la búsqueda
    """
    t = normalizar_texto(texto.strip())
    resultados = []
    for p in paises:
        if t in normalizar_texto(p["nombre"]):
            resultados.append(p)
    return resultados

def filtrar_por_continente(paises, cont):
    """
    Filtra países por continente específico.
    
    Args:
        paises: lista de diccionarios con datos de países
        cont: nombre del continente a filtrar
    
    Returns:
        Lista de países del continente especificado
    """
    c = cont.strip().lower()
    resultados = []
    for p in paises:
        if p["continente"].lower() == c:
            resultados.append(p)
    return resultados

def filtrar_por_rango(paises, clave, minimo=None, maximo=None):
    """
    Filtra países por rango de valores en una clave específica.
    
    Args:
        paises: lista de diccionarios con datos de países
        clave: campo a filtrar (poblacion o superficie)
        minimo: valor mínimo del rango (None = sin límite inferior)
        maximo: valor máximo del rango (None = sin límite superior)
    
    Returns:
        Lista de países que cumplen con el rango especificado
    """
    res = []
    for p in paises:
        # Verificar límite inferior
        if minimo is not None and p[clave] < minimo:
            continue
        # Verificar límite superior
        if maximo is not None and p[clave] > maximo:
            continue
        res.append(p)
    return res

def ordenar(paises, clave, descendente=False):
    """
    Ordena la lista de países según la clave especificada.
    
    Args:
        paises: lista de diccionarios con datos de países
        clave: campo por el cual ordenar (nombre, poblacion, superficie)
        descendente: True para orden descendente, False para ascendente
    
    Returns:
        Lista ordenada de países
    """
    if clave not in ("nombre", "poblacion", "superficie"):
        return paises[:]  # sin cambios si la clave no es válida
    
    # Función auxiliar para obtener el valor de ordenamiento
    def obtener_valor(pais):
        return pais[clave]
    
    return sorted(paises, key=obtener_valor, reverse=descendente)

def estadisticas(paises):
    """
    Calcula estadísticas generales sobre los países.
    
    Args:
        paises: lista de diccionarios con datos de países
    
    Returns:
        Diccionario con estadísticas calculadas o None si no hay datos
    """
    if not paises:
        return None
    
    # Función auxiliar para obtener población
    def obtener_poblacion(pais):
        return pais["poblacion"]
    
    # Calcular país con mayor y menor población
    mayor = max(paises, key=obtener_poblacion)
    menor = min(paises, key=obtener_poblacion)
    
    # Calcular promedios
    suma_pobl = 0
    suma_sup = 0
    for p in paises:
        suma_pobl += p["poblacion"]
        suma_sup += p["superficie"]
    
    prom_pobl = suma_pobl / len(paises)
    prom_sup = suma_sup / len(paises)
    
    # Contar países por continente
    por_cont = {}
    for p in paises:
        c = p["continente"]
        if c in por_cont:
            por_cont[c] = por_cont[c] + 1
        else:
            por_cont[c] = 1
    
    return {
        "mayor": mayor,
        "menor": menor,
        "prom_pobl": prom_pobl,
        "prom_sup": prom_sup,
        "por_cont": por_cont
    }