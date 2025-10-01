# sets_operaciones.py

# --- Creación de Sets ---
# Los sets se crean con llaves {} o con la función set().
# Su característica principal es que no permiten elementos duplicados [6].
lista_con_duplicados = ["Python", "Java", "C++", "Python", "Java"]
lenguajes_unicos = set(lista_con_duplicados)

print(f"Lista original: {lista_con_duplicados}")
print(f"Set a partir de la lista (sin duplicados): {lenguajes_unicos}\n")

# --- Operaciones Matemáticas de Conjuntos ---
# Esta es la gran fortaleza de los sets [7, 8].
materias_ana = {"Matemáticas", "Física", "Programación"}
materias_luis = {"Historia", "Programación", "Física"}

print(f"Materias de Ana: {materias_ana}")
print(f"Materias de Luis: {materias_luis}\n")

# 1. Intersección (&): Elementos que están en AMBOS sets [7, 9].
materias_comunes = materias_ana.intersection(materias_luis) # Alternativa: materias_ana & materias_luis
print(f"Materias en común (intersección): {materias_comunes}")

# 2. Unión (|): Todos los elementos de ambos sets, sin repetir [7, 9].
todas_las_materias = materias_ana.union(materias_luis) # Alternativa: materias_ana | materias_luis
print(f"Todas las materias (unión): {todas_las_materias}")

# 3. Diferencia (-): Elementos que están en el primer set, pero NO en el segundo [7, 9].
materias_solo_ana = materias_ana.difference(materias_luis) # Alternativa: materias_ana - materias_luis
print(f"Materias que solo cursa Ana (diferencia): {materias_solo_ana}\n")

# --- Métodos para Modificar Sets ---
# A pesar de que los elementos de un set deben ser inmutables, el set en sí es mutable [3].

# .add(): Agrega un solo elemento. Si ya existe, no hace nada.
print(f"Set original de Ana: {materias_ana}")
materias_ana.add("Química")
materias_ana.add("Física") # No se agregará de nuevo
print(f"Ana agrega 'Química' y trata de agregar 'Física' de nuevo: {materias_ana}")

# .update(): Agrega múltiples elementos de otro iterable (lista, tupla, set).
nuevas_materias = {"Arte", "Literatura"}
materias_ana.update(nuevas_materias)
print(f"Ana agrega 'Arte' y 'Literatura': {materias_ana}\n")

# .remove() y .discard(): Eliminan un elemento.
# .remove() lanza un error (KeyError) si el elemento no existe.
materias_ana.remove("Matemáticas")
print(f"Set de Ana después de eliminar 'Matemáticas' con .remove(): {materias_ana}")
# materias_ana.remove("Inglés") # Esto daría un error

# .discard() es más seguro, ya que no lanza error si el elemento no se encuentra.
materias_ana.discard("Física")
materias_ana.discard("Inglés") # No hace nada, pero no falla.
print(f"Set de Ana después de eliminar 'Física' con .discard(): {materias_ana}")