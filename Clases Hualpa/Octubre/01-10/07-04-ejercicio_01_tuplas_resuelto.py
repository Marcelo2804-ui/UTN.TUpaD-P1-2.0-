# ejercicio_01_tuplas_resuelto.py

#Enunciado:
#Crea un programa que modele la configuración de un servidor utilizando tuplas.

#Define constantes para representar el nombre del servidor, el puerto y si está activo.

#Implementa una función que reciba estos datos y retorne una tupla con la configuración.

#Implementa otra función que reciba la tupla, la desempaquete y muestre un reporte en pantalla indicando si el servidor está activo o inactivo.

#En el algoritmo principal, crea la configuración y luego genera el reporte.



# Constantes para evitar "números mágicos"
NOMBRE_SERVIDOR = "servidor-db-01"
PUERTO_SERVIDOR = 5432
ESTADO_ACTIVO = True

def crear_configuracion_servidor(nombre, puerto, activo):
    """
    Crea una tupla con la configuración del servidor.
    Las tuplas son ideales aquí porque la configuración
    es un conjunto de datos fijos que no debería cambiar [1].
    """
    return (nombre, puerto, activo)

def mostrar_reporte_servidor(configuracion):
    """
    Recibe una tupla de configuración, la desempaqueta y muestra un reporte.
    El desempaquetado hace el código más legible que usar índices como configuracion.
    """
    # Desempaquetado de la tupla en variables descriptivas
    servidor, puerto, activo = configuracion

    # Usamos un operador ternario para definir el texto del estado
    estado_texto = "activo" if activo else "inactivo"
    
    print("--- Reporte de Estado del Servidor ---")
    print(f"El servidor '{servidor}' en el puerto '{puerto}' está {estado_texto}.")

# --- Algoritmo Principal ---
# 1. Creamos la tupla de configuración llamando a nuestra función.
config_servidor = crear_configuracion_servidor(NOMBRE_SERVIDOR, PUERTO_SERVIDOR, ESTADO_ACTIVO)

# 2. Mostramos el reporte pasando la tupla a la función correspondiente.
mostrar_reporte_servidor(config_servidor)