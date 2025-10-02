# ejercicio_02_sets_resuelto.py


#Enunciado:
#Desarrolla un programa que analice etiquetas de un post en comparación con las etiquetas que sigue un usuario, usando conjuntos (sets).

# Dada una lista de etiquetas de un post (con posibles duplicados), conviértela en un set para obtener solo las etiquetas únicas.

# Implementa una función que reciba el set del post y el set del usuario, y devuelva:

# Las etiquetas que coinciden (intersección).

# Todas las etiquetas combinadas (unión).

# Muestra un reporte con:

# Etiquetas únicas del post.

# Etiquetas que sigue el usuario.

# Intereses comunes.

# Universo de temas combinados.


# Datos de entrada (constantes)
ETIQUETAS_POST = ["python", "desarrollo", "web", "python", "tutorial"]
ETIQUETAS_USUARIO = {"python", "ia", "datos"}

def obtener_etiquetas_unicas(lista_etiquetas):
    """
    Convierte una lista a un set para eliminar duplicados automáticamente.
    Los sets son la herramienta perfecta y más eficiente para esta tarea [6].
    """
    return set(lista_etiquetas)

def analizar_coincidencias(set_post, set_usuario):
    """
    Realiza operaciones de conjuntos para encontrar etiquetas comunes y todas las etiquetas.
    Las operaciones de intersección y unión son extremadamente rápidas con sets [7].
    """
    # Intersección (&): encuentra las etiquetas presentes en ambos sets [9].
    coincidentes = set_post.intersection(set_usuario)
    
    # Unión (|): combina todas las etiquetas de ambos sets, sin duplicados [9].
    todas = set_post.union(set_usuario)
    
    return coincidentes, todas

def mostrar_reporte_etiquetas(coincidentes, todas, set_post, set_usuario):
    """
    Imprime un reporte claro y formateado de los resultados.
    """
    print("--- Análisis de Etiquetas ---")
    print(f"Etiquetas del post (únicas): {set_post}")
    print(f"Etiquetas que sigue el usuario: {set_usuario}\n")
    print(f"Etiquetas que coinciden (intereses comunes): {coincidentes}")
    print(f"Todas las etiquetas combinadas (universo de temas): {todas}")

# --- Algoritmo Principal ---
# 1. Limpiamos las etiquetas del post eliminando duplicados con un set.
etiquetas_post_unicas = obtener_etiquetas_unicas(ETIQUETAS_POST)

# 2. Realizamos el análisis de coincidencias usando los dos sets.
etiquetas_coincidentes, todas_las_etiquetas = analizar_coincidencias(etiquetas_post_unicas, ETIQUETAS_USUARIO)

# 3. Mostramos el reporte final con los resultados obtenidos.
mostrar_reporte_etiquetas(etiquetas_coincidentes, todas_las_etiquetas, etiquetas_post_unicas, ETIQUETAS_USUARIO)