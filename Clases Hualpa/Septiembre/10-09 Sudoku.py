import random # Realizado por el profesor

# ------------------------------
# Funciones auxiliares
# ------------------------------

def generar_tablero():
    """Genera un tablero 4x4 con números del 1 al 4 (pueden repetirse)."""
    return [[random.randint(1, 4) for _ in range(4)] for _ in range(4)]

def imprimir_tablero(tablero):
    """Muestra el tablero en forma de matriz con índices para el usuario.""" 
    print("   0   1   2   3")
    print("  ---------------")
    for i, fila in enumerate(tablero):
        print(i, "|", fila)
    print()

def validar_fila(tablero, fila):
    return len(set(tablero[fila])) == len(tablero[fila]) # fila desordenada con numero unico

def validar_columna(tablero, col):
    columna = [tablero[f][col] for f in range(4)]
    return len(set(columna)) == len(columna)

def validar_subcuadro(tablero, start_row, start_col):
    numeros = []
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            numeros.append(tablero[i][j])
    return len(set(numeros)) == len(numeros)

def tablero_valido(tablero):
    """Valida todas las filas, columnas y subcuadros."""
    for i in range(4):
        if not validar_fila(tablero, i):
            return False
        if not validar_columna(tablero, i):
            return False
    for r in [0, 2]:
        for c in [0, 2]:
            if not validar_subcuadro(tablero, r, c):
                return False
    return True

# ------------------------------
# Programa principal
# ------------------------------

tablero = generar_tablero()
print("Tablero inicial:")
imprimir_tablero(tablero)

while not tablero_valido(tablero):
    try:
        fila = int(input("Ingrese la fila (0-3): "))
        col = int(input("Ingrese la columna (0-3): "))
        nuevo_valor = int(input("Ingrese un valor entre 1 y 4: "))

        if 0 <= fila <= 3 and 0 <= col <= 3 and 1 <= nuevo_valor <= 4:
            tablero[fila][col] = nuevo_valor
            print("\nTablero actualizado:")
            imprimir_tablero(tablero)
        else:
            print("❌ Coordenadas o valor fuera de rango. Intente de nuevo.\n")

    except ValueError:
        print("❌ Entrada inválida. Debe ingresar números.\n")

print("✅ ¡Felicidades! Tablero válido completado:")
imprimir_tablero(tablero)
