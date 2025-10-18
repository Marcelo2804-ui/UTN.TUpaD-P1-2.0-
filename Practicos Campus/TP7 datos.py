'''
1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 
'''

print("\nEjercicio 1\n")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)



'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de 
ejecutar el código desarrollado en el punto anterior, actualizar los 
precios de las siguientes frutas:
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800
'''

print("\n\nEjercicio 2\n")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)



'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de 
ejecutar el código desarrollado en el punto anterior, crear una lista 
que contenga únicamente las frutas sin los precios. 
'''

print("\n\nEjercicio 3\n")

lista_frutas = list(precios_frutas)

print(lista_frutas)



'''
4) Escribí un programa que permita almacenar y consultar números 
telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y 
número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe.

Ejemplo:
contactos = {"Juan": "123456"}, "Ana": "987654"}
# Consultar: "Juan" -> muestra "123456"
'''

print("\n\nEjercicio 4\n")

dict_numeros = {}
for i in range(5):
    nombre = input("Ingresar nombre: ")
    numero = int(input("Ingresar número telefónico: "))
    dict_numeros[nombre] = numero

nombre = input("\nIngresar nombre para consultar número: ")
if (nombre in dict_numeros):
    print(f"{nombre} tiene el número telefónico {dict_numeros[nombre]}")
else:
    print("Ese nombre no existe en el diccionario")



'''
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.

Ejemplo:
#Entrada -> "hola mundo hola"
#Salida:
Palabras_unicas: {"hola", "mundo"}
Recuento: {"hola": 2, "mundo": 1}
'''

print("\n\nEjercicio 5\n")

frase = str(input("Ingresar una frase: "))

set_frase = set(frase.split(" "))
dict_frase = {}

for palabra in frase.split(" "):
    if palabra in dict_frase:
        dict_frase[palabra] += 1
    else:
        dict_frase[palabra] = 1

print(f"Set\n {set_frase}")
print(f"Dict\n {dict_frase}")



'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla 
de 3 notas. Luego, mostrá el promedio de cada alumno.

Ejemplo:
alumnos = {
    "Sofía": (10, 9, 8)
    "Luis": (6, 7, 7)
}
'''

print("\n\nEjercicio 6\n")

dict_alumnos = {}

for i in range(3):
    nombre = input("Ingresar nombre: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingresar {j+1}° nota de {nombre}: "))
        notas.append(nota)
    notas = tuple(notas)
    dict_alumnos[nombre] = notas

print(dict_alumnos)



'''
7) Dado dos sets de números, representando dos listas de estudiantes 
que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un 
parcial (sin repetir).
'''

print("\n\nEjercicio 7\n")

set_parcial1 = {"Juan", "Marcelo", "Tiago", "Enrique", "Luis"}
set_parcial2 = {"Juan", "Tiago", "Luis", "Pablo", "Matias"}

print(f"Estudiantes que aprobaron ambos parciales:")
print({set_parcial1.intersection(set_parcial2)})
print(f"Estudiantes que aprobaron solo un parcial:")
print({set_parcial1.symmetric_difference(set_parcial2)})
print(f"Estudiantes que aprobaron al menos un parcial:")
print({set_parcial1.union(set_parcial2)})



'''
8) Armá un diccionario donde las claves sean nombres de productos y los 
valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe. 
'''

print("\n\nEjercicio 8\n")

menu = '''--- Menu ---
1) Consultar stock de producto
2) Agregar unidades
3) Agregar producto
0) Salir'''

dict_productos = {}
while True:
    print(menu)
    opcion = input("\nIngresar opción: ")
    if opcion.isdigit():
        opcion = int(opcion)
    match(opcion):
        case 1:
            producto = input("\nIngresar producto: ")
            if (producto in dict_productos):
                print(f"Stock '{producto}': {dict_productos[producto]}")
            else:
                print("No se encuentra el producto en el diccionario")
        case 2:
            producto = input("\nIngresar producto: ")
            if (producto in dict_productos):
                unidades = input("Ingresar unidades")
                if (unidades.isdigit()):
                    unidades = int(unidades)
                    if (unidades >= 1):
                        dict_productos[producto] += unidades
                        print("Unidades agregadas")
                    else:
                        print("Dato inválido")
                else:
                    print("Dato inválido")
            else:
                print("No se encuentra el producto en el diccionario")
        case 3:
            producto = input("\nIngresar producto: ")
            if (producto not in dict_productos):
                dict_productos[producto] = 0
                print(f"Producto '{producto}' agregado")
            else:
                print("Ya se encuentra el producto en el diccionario")
        case 0:
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")



'''
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los 
valores sean eventos.

Ejemplo:
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes"", "15:00"): "Clase de inglés"
}

Permití consultar qué actividad hay en cierto día y hora. 
'''

print("\n\nEjercicio 9")

menu = '''\n--- Menu ---
1) Consultar evento
2) Agregar evento
0) Salir'''

dict_eventos = {}
while True:
    print(menu)
    opcion = input("\nIngresar opción: ")
    if opcion.isdigit():
        opcion = int(opcion)
    match(opcion):
        case 1:
            dia_semana = input("\nIngresar día de semana: ").lower()
            horario = input("Ingresar hora y minutos (XX:YY): ")
            tupla = (dia_semana, horario)
            if (tupla in dict_eventos):
                print(f"{tupla}: {dict_eventos[tupla]}")
            else:
                print("No se encuentra el evento en el diccionario " \
                "o hay datos inválidos")
        case 2:
            dia_semana = input("\nIngresar día de semana: ").lower()
            if (dia_semana not in ["lunes", "martes", "miercoles", 
                                "jueves", "viernes", "sabado", 
                                "domingo"]):
                print("Dato inválido\n")
                continue
            horario = input("Ingresar hora y minutos (XX:YY): ")
            if (not horario.split(":")[0].isdigit() or 
                not horario.split(":")[1].isdigit()):
                print("Dato inválido\n")
                continue
            elif (not (0 <= int(horario.split(":")[0]) <= 23) or 
                not (0 <= int(horario.split(":")[1]) <= 59)):
                print("Dato inválido\n")
                continue
            tupla = (dia_semana, horario)
            if (tupla not in dict_eventos):
                evento = input("Ingresar evento: ")
                dict_eventos[tupla] = evento
                print("Evento agregado")
            else:
                print("Ya se encuentra ocupado ese día y horario")
        case 0:
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")
    print("")



'''
10) Dado un diccionario que mapea nombres de países con sus capitales, 
construí un nuevo diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores.

Ejemplo:
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
'''

print("\n\nEjercicio 10\n")

original = {"Argentina": "Buenos Aires", 
            "Chile": "Santiago de Chile",
            "Bolivia": "Sucre",
            "Brasil": "Brasilia",
            "Colombia": "Bogotá",
            "Ecuador": "Quito",
            "Paraguay": "Asunción",
            "Perú": "Lima",
            "Uruguay": "Montevideo",
            "Venezuela": "Caracas"}
invertido = {}

for pais in original:
    invertido[original[pais]] = pais

print(invertido)