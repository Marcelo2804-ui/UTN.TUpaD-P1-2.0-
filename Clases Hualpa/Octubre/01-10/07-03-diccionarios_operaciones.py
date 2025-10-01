# diccionarios_operaciones.py

# --- Creación de Diccionarios ---
# Los diccionarios asocian una clave única a un valor. Son ideales para
# representar objetos con propiedades [2, 10].
estudiante = {
    "nombre": "Lucía",
    "edad": 20,
    "carrera": "Informática",
    "materias": ["Programación", "Cálculo", "Física"]
}
print(f"Diccionario del estudiante:\n{estudiante}\n")

# --- Acceso a Valores por Clave ---
# Se accede a los valores usando la clave entre corchetes [3].
nombre_estudiante = estudiante["nombre"]
print(f"Nombre del estudiante: {nombre_estudiante}\n")

# Acceso seguro con .get(): Evita errores si la clave no existe [4, 11].
# Si la clave 'promedio' no existe, devuelve None en lugar de un error.
promedio = estudiante.get("promedio")
print(f"Promedio del estudiante (con .get()): {promedio}")

# Podemos proveer un valor por defecto si la clave no se encuentra.
promedio_default = estudiante.get("promedio", "No asignado")
print(f"Promedio del estudiante (con .get() y valor por defecto): {promedio_default}\n")

# --- Modificación y Adición de Pares Clave-Valor ---
# Los diccionarios son mutables [10].
# Modificar un valor existente:
estudiante["edad"] = 21
print(f"Edad actualizada: {estudiante['edad']}")

# Agregar un nuevo par clave-valor:
estudiante["promedio"] = 8.75
print(f"Diccionario con promedio agregado:\n{estudiante}\n")

# --- Eliminación de Pares Clave-Valor ---
# Se puede usar 'del' o el método .pop().
del estudiante["carrera"]
print(f"Diccionario sin la clave 'carrera':\n{estudiante}\n")

# .pop() elimina la clave y devuelve su valor, útil si necesitamos usarlo.
edad_eliminada = estudiante.pop("edad")
print(f"Se eliminó la edad: {edad_eliminada}")
print(f"Diccionario final:\n{estudiante}\n")

# --- Iteración sobre Diccionarios ---
# La forma más común es usar el método .items() para obtener clave y valor a la vez [3, 12].
print("--- Recorriendo el diccionario con .items() ---")
for clave, valor in estudiante.items():
    # .capitalize() es un método de string para poner la primera letra en mayúscula.
    print(f"{clave.capitalize()}: {valor}")

# También podemos iterar solo sobre las claves o los valores [11].
print("\n--- Solo claves ---")
for clave in estudiante.keys():
    print(clave)

print("\n--- Solo valores ---")
for valor in estudiante.values():
    print(valor)