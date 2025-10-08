def _es_entero_str(s: str) -> bool:
    s = s.strip()
    if s == "":
        return False
    if s[0] in "+-":
        s = s[1:]
    return s.isdigit()

def _es_float_str(s: str) -> bool:
    s = s.strip()
    if s == "":
        return False
    # Permitir +/-, un solo punto, y dígitos
    if s[0] in "+-":
        s_core = s[1:]
    else:
        s_core = s
    if s_core.count(".") > 1:
        return False
    if s_core.replace(".", "").isdigit() and s_core != ".":
        return True
    return False

def leer_entero(prompt: str, permitir_negativos: bool = True) -> int:
    while True:
        s = input(prompt).strip()
        if _es_entero_str(s):
            n = int(s)
            if not permitir_negativos and n < 0:
                print("Debe ser un entero no negativo.")
            else:
                return n
        else:
            print("Entrada inválida. Ingresá un entero (ej: 7, -3).")

def leer_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        if _es_float_str(s):
            return float(s)
        else:
            print("Entrada inválida. Ingresá un número (ej: 3.5, -2, 0).")

def leer_lista_enteros(prompt: str) -> list:
    """
    Lee una lista de enteros ingresados separados por espacios.
    No usa try/except: valida cada token.
    """
    while True:
        linea = input(prompt).strip()
        if linea == "":
            print("Ingresá al menos un número o 0 para lista vacía explícita.")
            continue
        if linea == "0":
            return []
        partes = linea.split()
        ok = True
        out = []
        for p in partes:
            if _es_entero_str(p):
                out.append(int(p))
            else:
                ok = False
                break
        if ok:
            return out
        print("Alguno de los valores no es entero. Probá de nuevo (ej: 1 2 3 4).")

def leer_lista_floats(prompt: str) -> list:
    """
    Lee una lista de floats (notas u otros) separados por espacios.
    Sin try/except.
    """
    while True:
        linea = input(prompt).strip()
        if linea == "":
            print("Ingresá al menos un número o 0 para lista vacía explícita.")
            continue
        if linea == "0":
            return []
        partes = linea.split()
        ok = True
        out = []
        for p in partes:
            if _es_float_str(p):
                out.append(float(p))
            else:
                ok = False
                break
        if ok:
            return out
        print("Alguno de los valores no es número. Probá de nuevo (ej: 8 7.5 9).")


# ===================
# Ejercicio 1
# ===================
# Objetivo: tabla_multiplicar(n) -> lista del 1 al 10 para n>0

def tabla_multiplicar(n: int) -> list:
    """
    Devuelve la tabla de multiplicar de n (1..10).
    Si n <= 0, devuelve lista vacía (decisión simple).
    """
    if n <= 0:
        return []
    return [n * i for i in range(1, 11)]


# ===================
# Ejercicio 2
# ===================
# Objetivo: suma_pares(lista_de_enteros) -> suma de los pares

def suma_pares(numeros: list) -> int:
    """
    Suma los números pares (int) de la lista.
    Ignora valores no enteros si los hubiera.
    """
    total = 0
    for x in numeros:
        if isinstance(x, int) and x % 2 == 0:
            total += x
    return total


# ===================
# Ejercicio 3
# ===================
# Objetivo: rectangulo(longitud, anchura) -> (area, perimetro)

def rectangulo(longitud: float, anchura: float) -> tuple:
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return (area, perimetro)


# ===================
# Ejercicio 4
# ===================
# Objetivo: convertir_temperatura(C, unidad destino 'F' o 'K')

def convertir_temperatura(celsius: float, unidad: str):
    u = unidad.strip().upper()
    if u == "F":
        return celsius * 9/5 + 32.0
    elif u == "K":
        return celsius + 273.15
    else:
        return None  # unidad no válida


# ===================
# Ejercicio 5
# ===================
# Objetivo: es_primo(n) -> True/False (n entero positivo)

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    # sin math.sqrt: paramos cuando i*i > n
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# ===================
# Ejercicio 6
# ===================
# Objetivo: promedio_calificaciones(lista 0..10) -> promedio o 0 si vacía

def promedio_calificaciones(notas: list) -> float:
    # Filtra notas en rango [0, 10]
    validas = []
    for x in notas:
        if isinstance(x, (int, float)) and 0 <= x <= 10:
            validas.append(float(x))
    if len(validas) == 0:
        return 0.0
    # promedio simple
    suma = 0.0
    for v in validas:
        suma += v
    return suma / len(validas)


# ===================
# Ejercicio 7
# ===================
# Objetivo: validar_entrada (entero no negativo) + factorial(n)

def validar_entrada(x) -> bool:
    return isinstance(x, int) and x >= 0

def factorial(n: int) -> int:
    if not validar_entrada(n):
        return -1  # señal de inválido
    if n == 0 or n == 1:
        return 1
    f = 1
    i = 2
    while i <= n:
        f = f * i
        i += 1
    return f


# ===================
# Ejercicio 8
# ===================
# Objetivo: es_divisible(a, b) y es_primo usando es_divisible

def es_divisible(n: int, d: int) -> bool:
    if d == 0:
        return False
    return n % d == 0

def es_primo_v2(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if es_divisible(n, 2):
        return False
    i = 3
    while i * i <= n:
        if es_divisible(n, i):
            return False
        i += 2
    return True


# ===================
# Ejercicio 9
# ===================
# Objetivo: convertir_a_fahrenheit, convertir_a_kelvin, menu_conversion

def convertir_a_fahrenheit(c: float) -> float:
    return c * 9/5 + 32.0

def convertir_a_kelvin(c: float) -> float:
    return c + 273.15

def menu_conversion() -> str:
    print("\n--- Menú Conversión ---")
    print("1) Celsius -> Fahrenheit")
    print("2) Celsius -> Kelvin")
    print("Otro) Cancelar")
    opcion = input("Elegí opción: ").strip()
    if opcion == "1":
        return "F"
    elif opcion == "2":
        return "K"
    else:
        return ""  # inválida/cancelada


# ===================
# Ejercicio 10
# ===================
# Objetivo: validar_dimensiones, calcular_area, calcular_perimetro

def validar_dimensiones(longitud: float, anchura: float) -> bool:
    return (isinstance(longitud, (int, float)) and isinstance(anchura, (int, float))
            and longitud > 0 and anchura > 0)

def calcular_area(longitud: float, anchura: float) -> float:
    return longitud * anchura

def calcular_perimetro(longitud: float, anchura: float) -> float:
    return 2 * (longitud + anchura)


# ===========================
# Drivers de demostración I/O
# ===========================

def demo_ej1():
    print("\n[Ej1] Tabla de multiplicar")
    n = leer_entero("Ingresá un entero positivo: ", permitir_negativos=False)
    if n <= 0:
        print("El número debe ser positivo.")
        return
    print("Tabla:", tabla_multiplicar(n))

def demo_ej2():
    print("\n[Ej2] Suma de números pares")
    nums = leer_lista_enteros("Lista de enteros (espacio). 0 para lista vacía: ")
    print("Suma de pares:", suma_pares(nums))

def demo_ej3():
    print("\n[Ej3] Área y perímetro de un rectángulo")
    L = leer_float("Longitud: ")
    A = leer_float("Anchura: ")
    area, perimetro = rectangulo(L, A)
    print(f"Área={area}, Perímetro={perimetro}")

def demo_ej4():
    print("\n[Ej4] Conversión de temperatura (C -> F o K)")
    c = leer_float("Celsius: ")
    u = input("Unidad destino (F/K): ").strip().upper()
    r = convertir_temperatura(c, u)
    if r is None:
        print("Unidad inválida.")
    else:
        print(f"Resultado: {r} {u}")

def demo_ej5():
    print("\n[Ej5] Verificador de número primo")
    n = leer_entero("Ingresá un entero: ")
    print(f"{n} es primo? {es_primo(n)}")

def demo_ej6():
    print("\n[Ej6] Promedio de calificaciones (0..10)")
    notas = leer_lista_floats("Notas separadas por espacio (0 para lista vacía): ")
    print("Promedio:", promedio_calificaciones(notas))

def demo_ej7():
    print("\n[Ej7] Factorial con validación")
    n = leer_entero("Entero no negativo: ", permitir_negativos=False)
    f = factorial(n)
    if f == -1:
        print("Entrada inválida.")
    else:
        print(f"{n}! = {f}")

def demo_ej8():
    print("\n[Ej8] Primos con función auxiliar es_divisible")
    n = leer_entero("Ingresá un entero: ")
    print(f"{n} es primo? {es_primo_v2(n)}")

def demo_ej9():
    print("\n[Ej9] Conversor de temperatura con menú")
    c = leer_float("Celsius: ")
    destino = menu_conversion()
    if destino == "F":
        print("Resultado:", convertir_a_fahrenheit(c), "F")
    elif destino == "K":
        print("Resultado:", convertir_a_kelvin(c), "K")
    else:
        print("Opción inválida o cancelada.")

def demo_ej10():
    print("\n[Ej10] Rectángulo con validación")
    L = leer_float("Longitud: ")
    A = leer_float("Anchura: ")
    if validar_dimensiones(L, A):
        print("Área:", calcular_area(L, A))
        print("Perímetro:", calcular_perimetro(L, A))
    else:
        print("Dimensiones inválidas (deben ser > 0).")


# ===================
# Tests rápidos
# ===================

def run_tests():
    print("\n[Tests] Ejecutando asserts rápidos...")
    # Ej1
    assert tabla_multiplicar(3) == [3,6,9,12,15,18,21,24,27,30]
    assert tabla_multiplicar(0) == []
    # Ej2
    assert suma_pares([1,2,3,4,5,6]) == 12
    assert suma_pares([]) == 0
    # Ej3
    assert rectangulo(2,4) == (8,12)
    # Ej4
    assert convertir_temperatura(0,"F") == 32.0
    assert convertir_temperatura(0,"K") == 273.15
    assert convertir_temperatura(0,"X") is None
    # Ej5
    assert es_primo(2) and es_primo(3) and es_primo(13)
    assert not es_primo(1) and not es_primo(9) and not es_primo(100)
    # Ej6
    assert abs(promedio_calificaciones([8.5,9.0,7.5,8.0]) - 8.25) < 1e-9
    assert promedio_calificaciones([]) == 0.0
    assert promedio_calificaciones([20,-1]) == 0.0  # fuera de rango -> ignora
    # Ej7
    assert factorial(0) == 1 and factorial(5) == 120
    assert factorial(-3) == -1
    # Ej8
    assert es_divisible(10,5) and not es_divisible(10,3)
    assert es_primo_v2(7) and not es_primo_v2(8)
    # Ej9
    assert abs(convertir_a_fahrenheit(0) - 32.0) < 1e-9
    assert abs(convertir_a_kelvin(0) - 273.15) < 1e-9
    # Ej10
    assert validar_dimensiones(2,3) and not validar_dimensiones(-1,3)
    assert calcular_area(2,3) == 6 and calcular_perimetro(2,3) == 10

    print("OK: todos los asserts pasaron.")


# ===================
# Main con menú simple
# ===================

def main():
    while True:
        print("\n=== Kata: Funciones en Python ===")
        print("1) Ej1 - Tabla de multiplicar")
        print("2) Ej2 - Suma de números pares")
        print("3) Ej3 - Área y perímetro rectángulo")
        print("4) Ej4 - Conversión C -> F/K")
        print("5) Ej5 - Verificador de primo")
        print("6) Ej6 - Promedio de calificaciones")
        print("7) Ej7 - Factorial con validación")
        print("8) Ej8 - Primos con es_divisible")
        print("9) Ej9 - Conversor con menú")
        print("10) Ej10 - Rectángulo con validación")
        print("0) Tests rápidos")
        print("q) Salir")
        op = input("Elegí opción: ").strip().lower()

        if op == "1":
            demo_ej1()
        elif op == "2":
            demo_ej2()
        elif op == "3":
            demo_ej3()
        elif op == "4":
            demo_ej4()
        elif op == "5":
            demo_ej5()
        elif op == "6":
            demo_ej6()
        elif op == "7":
            demo_ej7()
        elif op == "8":
            demo_ej8()
        elif op == "9":
            demo_ej9()
        elif op == "10":
            demo_ej10()
        elif op == "0":
            run_tests()
        elif op == "q":
            print("Nos vemos!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
