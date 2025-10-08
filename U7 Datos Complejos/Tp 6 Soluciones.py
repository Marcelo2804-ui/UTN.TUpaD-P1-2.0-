# TP 6: Resolución Completa

# --- Ejercicio 1: Añadir frutas ---
print("--- Ejercicio 1 y 2 ---")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print("Diccionario original:", precios_frutas)
# Añadimos las nuevas frutas 
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario con frutas añadidas:", precios_frutas)

# --- Ejercicio 2: Actualizar precios ---
# Actualizamos los precios de las frutas existentes [cite: 19]
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario con precios actualizados:", precios_frutas)
print("-" * 30)

# --- Ejercicio 3: Lista de frutas ---
print("--- Ejercicio 3 ---")
# Creamos una lista solo con las claves (frutas) 
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)
print("-" * 30)

# --- Ejercicio 4: Agenda telefónica ---
print("--- Ejercicio 4 ---")
contactos = {}
# Permitimos al usuario cargar 5 contactos 
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

print("\nAgenda de contactos creada:", contactos)

# Pedimos un nombre para consultar el número 
nombre_consulta = input("\nIngrese el nombre del contacto que desea consultar: ")
# Usamos .get() para mostrar el número o un mensaje si no existe
numero_encontrado = contactos.get(nombre_consulta, "El contacto no fue encontrado.")
print(f"Resultado de la búsqueda: {numero_encontrado}")
print("-" * 30)

# --- Ejercicio 5: Análisis de frase ---
print("--- Ejercicio 5 ---")
# Solicitamos una frase al usuario [cite: 33]
frase = input("Ingrese una frase: ")
palabras = frase.lower().split() # Convertimos a minúsculas y dividimos en palabras

# Usamos un set para obtener las palabras únicas 
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Creamos un diccionario para contar la frecuencia de cada palabra 
recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
print("Recuento de palabras:", recuento_palabras)
print("-" * 30)

# --- Ejercicio 6: Promedio de alumnos ---
print("--- Ejercicio 6 ---")
alumnos = {}
# Permitimos ingresar los nombres de 3 alumnos y sus notas 
for _ in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    # Pedimos las 3 notas en una sola línea, separadas por espacios
    notas_str = input(f"Ingrese las 3 notas de {nombre_alumno} separadas por un espacio: ")
    # Convertimos las notas a números y las guardamos en una tupla
    notas_tuple = tuple(map(int, notas_str.split()))
    alumnos[nombre_alumno] = notas_tuple

print("\n--- Promedios ---")
# Mostramos el promedio de cada alumno [cite: 42]
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}") # .2f formatea a 2 decimales
print("-" * 30)

# --- Ejercicio 7: Operaciones con sets ---
print("--- Ejercicio 7 ---")
# Sets de ejemplo con legajos de estudiantes
parcial_1 = {101, 102, 105, 107, 110, 115}
parcial_2 = {102, 106, 107, 111, 115, 120}
print("Aprobaron Parcial 1:", parcial_1)
print("Aprobaron Parcial 2:", parcial_2)

# Mostramos los que aprobaron ambos parciales (intersección) 
ambos_parciales = parcial_1.intersection(parcial_2)
print("\nEstudiantes que aprobaron ambos parciales:", ambos_parciales)

# Mostramos los que aprobaron solo uno de los dos (diferencia simétrica) 
solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)

# Mostramos la lista total de estudiantes que aprobaron al menos un parcial (unión) 
todos_aprobados = parcial_1.union(parcial_2)
print("Lista total de estudiantes que aprobaron al menos un parcial:", todos_aprobados)
print("-" * 30)


# --- Ejercicio 8: Gestión de stock ---
print("--- Ejercicio 8 ---")
stock = {"Arroz": 150, "Fideos": 200, "Aceite": 80}

while True:
    print("\n--- Menú de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        # Consultar stock [cite: 55]
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(f"El stock de {producto} es: {stock.get(producto, 'Producto no encontrado')}")
    elif opcion == '2':
        # Agregar unidades a un producto existente [cite: 56]
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock:
            unidades = int(input(f"¿Cuántas unidades de {producto} desea agregar?: "))
            stock[producto] += unidades
            print(f"Stock actualizado. Nuevo stock de {producto}: {stock[producto]}")
        else:
            print("El producto no existe. Use la opción 3 para agregarlo.")
    elif opcion == '3':
        # Agregar un nuevo producto [cite: 57]
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock:
            unidades = int(input(f"Ingrese el stock inicial para {producto}: "))
            stock[producto] = unidades
            print(f"Producto {producto} agregado con éxito.")
        else:
            print("El producto ya existe en el stock.")
    elif opcion == '4':
        print("Saliendo del programa de stock.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
print("Stock final:", stock)
print("-" * 30)

# --- Ejercicio 9: Agenda de eventos ---
print("--- Ejercicio 9 ---")
# La clave es una tupla (día, hora) 
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de Programación 1",
    ("jueves", "09:00"): "Entrega del TP6",
    ("viernes", "18:30"): "After office"
}

# Permitimos consultar una actividad 
dia_consulta = input("Ingrese el día a consultar (ej: lunes): ").lower()
hora_consulta = input("Ingrese la hora a consultar (ej: 10:00): ")

# Creamos la tupla para buscar en el diccionario
evento_buscado = (dia_consulta, hora_consulta)
actividad = agenda.get(evento_buscado, "No hay ninguna actividad programada en esa fecha y hora.")
print(f"Actividad: {actividad}")
print("-" * 30)


# --- Ejercicio 10: Invertir diccionario ---
print("--- Ejercicio 10 ---")
# Diccionario original de países y capitales [cite: 71]
paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo", "Perú": "Lima"}
print("Diccionario original:", paises_capitales)

invertido = {}
# Recorremos el diccionario original y lo invertimos
for pais, capital in paises_capitales.items():
    invertido[capital] = pais # La capital ahora es la clave y el país el valor 

print("Diccionario invertido:", invertido)
print("-" * 30)