"""
Sistema de Gestión de Ferretería
Repaso - Parcial 2
Autor: Scherer
Fecha: 27 de octubre de 2025

Este programa permite gestionar el inventario de una ferretería,
almacenando los datos en un archivo CSV para persistencia entre ejecuciones.
"""

import csv  # Módulo para trabajar con archivos CSV
import os   # Módulo para operaciones del sistema operativo

# Nombre del archivo donde se almacenarán los datos
ARCHIVO_CSV = "inventario.csv"

# Lista global que contendrá todas las herramientas en memoria
inventario = []


def cargar_desde_csv():
    """
    Lee el archivo CSV y carga todas las herramientas en la lista 'inventario'.
    
    Esta función se ejecuta al inicio del programa para recuperar los datos
    almacenados previamente. Si el archivo no existe, se crea uno nuevo.
    
    Maneja excepciones:
    - FileNotFoundError: Si el archivo no existe, se crea uno nuevo con encabezados
    - Exception: Cualquier otro error se captura y se muestra un mensaje
    """
    global inventario  # Utilizamos la variable global para modificarla
    inventario = []    # Limpiamos la lista antes de cargar
    
    try:
        # Intentamos abrir el archivo en modo lectura
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            # csv.DictReader convierte cada fila en un diccionario
            # usando la primera fila como nombres de las claves
            lector = csv.DictReader(archivo)
            
            # Recorremos cada fila del archivo
            for fila in lector:
                # Convertimos los valores de texto a los tipos correctos
                herramienta = {
                    'nombre': fila['nombre'],           # String (texto)
                    'stock': int(fila['stock']),        # Entero
                    'precio': float(fila['precio'])     # Float (decimal)
                }
                # Agregamos el diccionario a nuestra lista
                inventario.append(herramienta)
        
        print(f"✓ Datos cargados correctamente: {len(inventario)} herramientas.\n")
    
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos con los encabezados
        print("⚠ Archivo no encontrado. Creando nuevo archivo...")
        with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as archivo:
            # Definimos los nombres de las columnas
            campos = ['nombre', 'stock', 'precio']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()  # Escribe la primera fila con los nombres
        print("✓ Archivo creado exitosamente.\n")
    
    except Exception as e:
        # Capturamos cualquier otro error inesperado
        print(f"✗ Error al cargar archivo: {e}\n")


def guardar_en_csv():
    """
    Guarda todas las herramientas del inventario en el archivo CSV.
    
    Esta función sobrescribe completamente el archivo con los datos
    actuales que están en memoria (lista 'inventario').
    
    Es llamada cada vez que se modifica el inventario para mantener
    la persistencia de los datos.
    """
    try:
        # Abrimos el archivo en modo escritura (sobrescribe el contenido)
        with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as archivo:
            # Definimos las columnas del CSV
            campos = ['nombre', 'stock', 'precio']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribimos la primera fila con los nombres de las columnas
            escritor.writeheader()
            
            # Escribimos cada herramienta como una fila
            for herramienta in inventario:
                escritor.writerow(herramienta)
        
        print("✓ Cambios guardados en el archivo.\n")
    
    except Exception as e:
        # Capturamos errores de escritura
        print(f"✗ Error al guardar archivo: {e}\n")


def cargar_herramientas():
    """
    Permite registrar nuevas herramientas en el inventario.
    
    Solicita al usuario:
    - Nombre de la herramienta (texto)
    - Stock disponible (número entero positivo o 0)
    - Precio unitario (número decimal positivo)
    
    Valida que los datos ingresados sean correctos y agrega
    la herramienta tanto a la lista en memoria como al archivo CSV.
    """
    print("\n═══ CARGAR NUEVA HERRAMIENTA ═══")
    
    try:
        # Solicitamos el nombre de la herramienta
        nombre = input("Ingrese nombre: ").strip()
        
        # Validamos que el nombre no esté vacío
        if not nombre:
            print("✗ El nombre no puede estar vacío.")
            return
        
        # Verificamos si la herramienta ya existe en el inventario
        for herramienta in inventario:
            if herramienta['nombre'].lower() == nombre.lower():
                print(f"✗ La herramienta '{nombre}' ya existe en el inventario.")
                return
        
        # Solicitamos y validamos el stock (debe ser un entero >= 0)
        stock = int(input("Ingrese stock: "))
        if stock < 0:
            print("✗ El stock no puede ser negativo.")
            return
        
        # Solicitamos y validamos el precio (debe ser un número positivo)
        precio = float(input("Ingrese precio: "))
        if precio <= 0:
            print("✗ El precio debe ser mayor a cero.")
            return
        
        # Creamos el diccionario con los datos de la herramienta
        nueva_herramienta = {
            'nombre': nombre,
            'stock': stock,
            'precio': precio
        }
        
        # Agregamos la herramienta a la lista en memoria
        inventario.append(nueva_herramienta)
        
        # Guardamos los cambios en el archivo CSV
        guardar_en_csv()
        
        print("✓ Herramienta registrada correctamente.\n")
    
    except ValueError:
        # Error si el usuario ingresa texto donde se espera un número
        print("✗ Error: debe ingresar números válidos para stock y precio.\n")
    except Exception as e:
        # Capturamos cualquier otro error
        print(f"✗ Error inesperado: {e}\n")


def mostrar_herramientas():
    """
    Muestra todas las herramientas registradas en el inventario.
    
    Lee los datos directamente del archivo CSV (para asegurar que
    muestre la información más actualizada) y los presenta en un
    formato legible.
    
    Si no hay herramientas registradas, muestra un mensaje informativo.
    """
    print("\n═══ HERRAMIENTAS REGISTRADAS ═══")
    
    # Primero cargamos los datos más recientes del archivo
    cargar_desde_csv()
    
    # Verificamos si hay herramientas en el inventario
    if len(inventario) == 0:
        print("⚠ No hay herramientas registradas.\n")
        return
    
    # Mostramos cada herramienta con formato
    for herramienta in inventario:
        print(f"{herramienta['nombre']} → Stock: {herramienta['stock']} → Precio: ${herramienta['precio']}")
    
    print()  # Línea en blanco para mejor visualización


def modificar_herramienta():
    """
    Permite modificar el stock y/o precio de una herramienta existente.
    
    Busca la herramienta por nombre y permite actualizar:
    - Stock: nueva cantidad de unidades disponibles
    - Precio: nuevo valor unitario
    
    Los cambios se reflejan tanto en memoria como en el archivo CSV.
    """
    print("\n═══ MODIFICAR HERRAMIENTA ═══")
    
    # Verificamos si hay herramientas para modificar
    if len(inventario) == 0:
        print("⚠ No hay herramientas registradas para modificar.\n")
        return
    
    # Solicitamos el nombre de la herramienta a modificar
    nombre = input("Ingrese el nombre a modificar: ").strip()
    
    # Buscamos la herramienta en el inventario
    herramienta_encontrada = None
    for herramienta in inventario:
        # Comparamos ignorando mayúsculas/minúsculas
        if herramienta['nombre'].lower() == nombre.lower():
            herramienta_encontrada = herramienta
            break
    
    # Si no se encontró, mostramos mensaje y salimos
    if herramienta_encontrada is None:
        print(f"✗ No se encontró la herramienta '{nombre}'.\n")
        return
    
    try:
        # Solicitamos el nuevo stock
        nuevo_stock = int(input("Nuevo stock: "))
        if nuevo_stock < 0:
            print("✗ El stock no puede ser negativo.")
            return
        
        # Solicitamos el nuevo precio
        nuevo_precio = float(input("Nuevo precio: "))
        if nuevo_precio <= 0:
            print("✗ El precio debe ser mayor a cero.")
            return
        
        # Actualizamos los valores en el diccionario
        herramienta_encontrada['stock'] = nuevo_stock
        herramienta_encontrada['precio'] = nuevo_precio
        
        # Guardamos los cambios en el archivo
        guardar_en_csv()
        
        print("✓ Datos actualizados correctamente.\n")
    
    except ValueError:
        # Error si se ingresan valores no numéricos
        print("✗ Error: debe ingresar números válidos.\n")
    except Exception as e:
        print(f"✗ Error inesperado: {e}\n")


def eliminar_herramienta():
    """
    Elimina una herramienta del inventario por nombre.
    
    Busca la herramienta en la lista y la elimina tanto de la memoria
    como del archivo CSV.
    
    Solicita confirmación antes de realizar la eliminación.
    """
    print("\n═══ ELIMINAR HERRAMIENTA ═══")
    
    # Verificamos si hay herramientas para eliminar
    if len(inventario) == 0:
        print("⚠ No hay herramientas registradas para eliminar.\n")
        return
    
    # Solicitamos el nombre de la herramienta a eliminar
    nombre = input("Ingrese el nombre de la herramienta a eliminar: ").strip()
    
    # Buscamos la herramienta en el inventario
    herramienta_encontrada = None
    indice = -1
    
    for i, herramienta in enumerate(inventario):
        if herramienta['nombre'].lower() == nombre.lower():
            herramienta_encontrada = herramienta
            indice = i
            break
    
    # Si no se encontró, mostramos mensaje y salimos
    if herramienta_encontrada is None:
        print(f"✗ No se encontró la herramienta '{nombre}'.\n")
        return
    
    # Mostramos la información de la herramienta a eliminar
    print(f"\nHerramienta encontrada:")
    print(f"{herramienta_encontrada['nombre']} → Stock: {herramienta_encontrada['stock']} → Precio: ${herramienta_encontrada['precio']}")
    
    # Solicitamos confirmación
    confirmacion = input("\n¿Está seguro de eliminarla? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        # Eliminamos la herramienta de la lista usando el índice
        inventario.pop(indice)
        
        # Guardamos los cambios en el archivo
        guardar_en_csv()
        
        print("✓ Herramienta eliminada correctamente.\n")
    else:
        print("✓ Operación cancelada.\n")


def consultar_disponibilidad():
    """
    Consulta y muestra el stock disponible de una herramienta específica.
    
    Solicita el nombre de la herramienta y muestra:
    - Nombre
    - Cantidad de unidades disponibles (stock)
    - Precio unitario
    """
    print("\n═══ CONSULTAR DISPONIBILIDAD ═══")
    
    # Verificamos si hay herramientas registradas
    if len(inventario) == 0:
        print("⚠ No hay herramientas registradas.\n")
        return
    
    # Solicitamos el nombre de la herramienta
    nombre = input("Ingrese el nombre de la herramienta: ").strip()
    
    # Buscamos la herramienta
    herramienta_encontrada = None
    for herramienta in inventario:
        if herramienta['nombre'].lower() == nombre.lower():
            herramienta_encontrada = herramienta
            break
    
    # Mostramos el resultado
    if herramienta_encontrada:
        print(f"\n✓ {herramienta_encontrada['nombre']}")
        print(f"  Stock disponible: {herramienta_encontrada['stock']} unidades")
        print(f"  Precio: ${herramienta_encontrada['precio']}\n")
    else:
        print(f"✗ No se encontró la herramienta '{nombre}'.\n")


def listar_sin_stock():
    """
    Lista todas las herramientas que tienen stock igual a 0.
    
    Útil para identificar qué productos necesitan reposición.
    Si no hay productos sin stock, muestra un mensaje informativo.
    """
    print("\n═══ HERRAMIENTAS SIN STOCK ═══")
    
    # Creamos una lista con las herramientas que tienen stock = 0
    sin_stock = []
    for herramienta in inventario:
        if herramienta['stock'] == 0:
            sin_stock.append(herramienta)
    
    # Verificamos si encontramos herramientas sin stock
    if len(sin_stock) == 0:
        print("✓ Todas las herramientas tienen stock disponible.\n")
    else:
        print(f"⚠ Se encontraron {len(sin_stock)} herramienta(s) sin stock:\n")
        for herramienta in sin_stock:
            print(f"  • {herramienta['nombre']} → Precio: ${herramienta['precio']}")
        print()


def mostrar_menu():
    """
    Muestra el menú principal del sistema con todas las opciones disponibles.
    
    Presenta las opciones de forma clara y estructurada para que el usuario
    pueda seleccionar la funcionalidad que desea utilizar.
    """
    print("╔════════════════════════════════╗")
    print("║    MENÚ FERRETERÍA             ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Cargar herramientas         ║")
    print("║ 2. Mostrar herramientas        ║")
    print("║ 3. Modificar herramienta       ║")
    print("║ 4. Eliminar herramienta        ║")
    print("║ 5. Consultar disponibilidad    ║")
    print("║ 6. Listar sin stock            ║")
    print("║ 7. Salir                       ║")
    print("╚════════════════════════════════╝")


def main():
    """
    Función principal que ejecuta el programa.
    
    Carga los datos al inicio, muestra el menú en un bucle infinito,
    y ejecuta la opción seleccionada por el usuario hasta que decida salir.
    
    El bucle se mantiene activo (while True) y solo se termina cuando
    el usuario selecciona la opción 7 (Salir).
    """
    print("\n" + "="*40)
    print("  SISTEMA DE GESTIÓN DE FERRETERÍA")
    print("="*40 + "\n")
    
    # Cargamos los datos existentes del archivo CSV al inicio
    cargar_desde_csv()
    
    # Bucle principal del programa
    while True:
        # Mostramos el menú
        mostrar_menu()
        
        try:
            # Solicitamos la opción al usuario
            opcion = input("\nSeleccione una opción (1-7): ").strip()
            
            # Evaluamos la opción seleccionada
            if opcion == '1':
                cargar_herramientas()
            
            elif opcion == '2':
                mostrar_herramientas()
            
            elif opcion == '3':
                modificar_herramienta()
            
            elif opcion == '4':
                eliminar_herramienta()
            
            elif opcion == '5':
                consultar_disponibilidad()
            
            elif opcion == '6':
                listar_sin_stock()
            
            elif opcion == '7':
                # Opción para salir del programa
                print("\n" + "="*40)
                print("  Gracias por usar el sistema")
                print("  Todos los cambios han sido guardados")
                print("="*40 + "\n")
                break  # Salimos del bucle while, finalizando el programa
            
            else:
                # Si el usuario ingresa una opción no válida
                print("✗ Opción no válida. Por favor, elija entre 1 y 7.\n")
        
        except Exception as e:
            # Capturamos cualquier error inesperado
            print(f"✗ Error: {e}\n")


# Punto de entrada del programa
# Este bloque se ejecuta solo si el archivo se ejecuta directamente
# (no si se importa como módulo)
if __name__ == "__main__":
    main()
