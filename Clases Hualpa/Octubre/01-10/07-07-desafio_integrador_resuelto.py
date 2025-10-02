# desafio_integrador_resuelto.py


# Enunciado:
# Se dispone de una lista de inscripciones de estudiantes a distintos cursos.
# Cada inscripción está representada por una tupla con el formato:
# (id_estudiante, nombre_curso, categoría)
# Algunos registros están duplicados.

# Se pide desarrollar un programa que:

# Elimine las inscripciones duplicadas utilizando un set.

# Filtre únicamente los cursos de la categoría "Programación".

# Cuente cuántos estudiantes únicos están inscriptos en cada curso, 
# utilizando un diccionario cuya clave sea el nombre del curso y
# el valor un set con los IDs de los estudiantes.

# Genere un reporte final en pantalla con el nombre de cada curso de programación 
# y la cantidad de estudiantes únicos inscriptos.




# Datos de entrada
INSCRIPCIONES = [
    (101, "Programación 1", "Programación"),
    (102, "Bases de Datos", "Programación"),
    (101, "Inglés Técnico", "Idiomas"),
    (103, "Cálculo 1", "Matemáticas"),
    (102, "Programación 1", "Programación"),  # Inscripción duplicada
    (104, "Álgebra", "Matemáticas"),
    (101, "Programación 1", "Programación"),  # Otra duplicada
]

# Constante para el filtrado
CATEGORIA_OBJETIVO = "Programación"

def eliminar_inscripciones_duplicadas(inscripciones):
    """
    Paso 1: Usa un set para eliminar tuplas duplicadas de la lista.
    Como las tuplas son inmutables, pueden ser elementos de un set.
    Esta es la forma más eficiente de obtener registros únicos [2, 6].
    Retorna una lista de tuplas únicas para mantener el orden si es necesario.
    """
    print("Paso 1: Eliminando duplicados...")
    inscripciones_unicas_set = set(inscripciones)
    print(f"Se encontraron {len(inscripciones_unicas_set)} inscripciones únicas.\n")
    return list(inscripciones_unicas_set)

def filtrar_por_categoria(inscripciones, categoria):
    """
    Paso 2: Recorre las inscripciones únicas y filtra solo las de la categoría deseada.
    Aquí usamos una lista por comprensión, una forma concisa y eficiente de crear
    una nueva lista basada en una condición [12].
    """
    print(f"Paso 2: Filtrando cursos de la categoría '{categoria}'...")
    # La tupla se desempaqueta en el 'for' para hacer la condición más legible.
    cursos_filtrados = [
        insc for insc in inscripciones 
        if insc[2] == categoria
    ]
    print(f"Se encontraron {len(cursos_filtrados)} inscripciones de programación.\n")
    return cursos_filtrados

def contar_estudiantes_por_curso(inscripciones_filtradas):
    """
    Paso 3: Cuenta cuántos estudiantes únicos hay por cada curso.
    Un diccionario es perfecto para esta tarea:
    - Clave: El nombre del curso (único).
    - Valor: Un set para almacenar los IDs de los estudiantes (garantiza unicidad).
    """
    print("Paso 3: Contando estudiantes por curso...")
    conteo_por_curso = {}
    
    for id_estudiante, nombre_curso, _ in inscripciones_filtradas:
        # Si el curso no está en el diccionario, lo inicializamos con un set vacío.
        # .setdefault() hace esto de forma elegante [11].
        conteo_por_curso.setdefault(nombre_curso, set()).add(id_estudiante)
    
    print("Conteo finalizado.\n")
    return conteo_por_curso

def generar_reporte_final(conteo):
    """
    Paso 4: Recorre el diccionario de conteo y genera un reporte final.
    Iteramos sobre .items() para obtener la clave (curso) y el valor (set de IDs) [3].
    La cantidad de inscriptos es simplemente el tamaño (len) del set.
    """
    print("--- Reporte Final de Inscripciones en Programación ---")
    if not conteo:
        print("No se encontraron inscripciones para la categoría especificada.")
        return
        
    for curso, estudiantes_ids in conteo.items():
        cantidad_inscriptos = len(estudiantes_ids)
        print(f"Curso: {curso} - Inscriptos únicos: {cantidad_inscriptos}")

# --- Algoritmo Principal ---
# Se encadenan las funciones, pasando el resultado de una como entrada a la siguiente.
inscripciones_unicas = eliminar_inscripciones_duplicadas(INSCRIPCIONES)
cursos_programacion = filtrar_por_categoria(inscripciones_unicas, CATEGORIA_OBJETIVO)
conteo_cursos = contar_estudiantes_por_curso(cursos_programacion)
generar_reporte_final(conteo_cursos)
print("")
print("----------------------------------")
print("")
generar_reporte_final(contar_estudiantes_por_curso(filtrar_por_categoria(eliminar_inscripciones_duplicadas(INSCRIPCIONES),CATEGORIA_OBJETIVO)))