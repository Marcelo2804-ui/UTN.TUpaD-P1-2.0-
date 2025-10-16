import csv

def cargar_datos_csv(ruta_archivo):
    """
    Lee el archivo CSV y lo convierte en una lista de diccionarios.
    """
    paises = []
    try:
        # Abrimos el archivo en modo lectura ('r') de forma segura
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            
            # Saltamos la primera línea del archivo, que es el encabezado
            next(lector_csv)

            # Recorremos cada fila de datos del archivo
            for fila in lector_csv:
                # Creamos un diccionario para este país
                pais = {
                    'nombre': fila[0],
                    'poblacion': int(fila[1]), # Convertimos el texto a número
                    'superficie': int(fila[2]), # Convertimos el texto a número
                    'continente': fila[3]
                }
                # Agregamos el país a nuestra lista principal
                paises.append(pais)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")
    
    return paises

# --- Bloque para probar que todo funcione ---
# Este código solo se ejecuta cuando corrés este archivo
if __name__ == "__main__":
    lista_de_paises = cargar_datos_csv('paises.csv')
    
    if lista_de_paises:
        print("¡Datos cargados exitosamente! ✅")
        print("--- Verificando los primeros 2 países: ---")
        print(lista_de_paises[0])
        print(lista_de_paises[1])