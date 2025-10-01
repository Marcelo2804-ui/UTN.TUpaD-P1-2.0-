# tuplas_operaciones.py

# --- Creación de Tuplas ---
# Las tuplas se definen con paréntesis y son ideales para datos fijos
# que no deben cambiar, como coordenadas o constantes [1, 2].
coordenadas_gps = (34.56, -58.47)
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print(f"Coordenadas: {coordenadas_gps}")
print(f"Días de la semana: {dias_semana}\n")

# --- Acceso a Elementos por Índice ---
# Al ser ordenadas, podemos acceder a sus elementos con un índice, igual que en las listas [1, 3].
PRIMER_DIA_INDICE = 0
latitud = coordenadas_gps[PRIMER_DIA_INDICE]
print(f"La latitud es: {latitud}")
print(f"El primer día de la semana es: {dias_semana[PRIMER_DIA_INDICE]}\n")

# --- Inmutabilidad (Característica Clave) ---
# Si intentamos modificar un elemento de una tupla, Python lanzará un error (TypeError).
# Esto las hace seguras para datos sensibles [1, 4].
# La siguiente línea está comentada porque detendría el programa:
# dias_semana = "Otro día"  # Esto generaría: TypeError: 'tuple' object does not support item assignment

# --- Métodos Comunes de las Tuplas ---

# 1. .count(): Cuenta cuántas veces aparece un elemento en la tupla [5].
colores_repetidos = ("rojo", "azul", "verde", "rojo", "amarillo", "rojo")
cantidad_rojo = colores_repetidos.count("rojo")
print(f"La tupla de colores es: {colores_repetidos}")
print(f"El color 'rojo' aparece {cantidad_rojo} veces.\n")

# 2. .index(): Devuelve el índice de la primera aparición de un elemento [5].
indice_azul = colores_repetidos.index("azul")
print(f"El color 'azul' se encuentra por primera vez en el índice: {indice_azul}\n")

# --- Desempaquetado de Tuplas ---
# Una forma muy "pythónica" de asignar los valores de una tupla a variables individuales.
nombre, categoria, precio = ("Laptop Gamer", "Electrónica", 1500)
print("--- Desempaquetado de Tupla ---")
print(f"Producto: {nombre}")
print(f"Categoría: {categoria}")
print(f"Precio: ${precio}\n")

# --- Iteración sobre Tuplas ---
# Podemos recorrer una tupla con un bucle 'for' como si fuera una lista.
print("Recorriendo los días de la semana:")
for dia in dias_semana:
    print(f"- {dia}")
