"""
TP7 - RECURSIVIDAD
Tecnicatura Universitaria en Programación
Programación I

Ejercicios de aplicación de recursividad
"""

# ============================================================================
# EJERCICIO 1: Factorial recursivo
# ============================================================================

def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: Factorial de n
    """
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)


def ejercicio1():
    """
    Calcula y muestra el factorial de todos los números entre 1 y el número
    que indique el usuario.
    """
    print("\n" + "="*60)
    print("EJERCICIO 1: Factorial de un número")
    print("="*60)
    
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        if numero < 1:
            print("Error: Debe ingresar un número mayor o igual a 1")
            return
        
        print(f"\nFactoriales desde 1 hasta {numero}:")
        print("-" * 40)
        
        for i in range(1, numero + 1):
            resultado = factorial(i)
            print(f"Factorial de {i}: {resultado}")
            
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


# ============================================================================
# EJERCICIO 2: Serie de Fibonacci
# ============================================================================

def fibonacci(n):
    """
    Calcula el valor de la serie de Fibonacci en la posición n de forma recursiva.
    
    Args:
        n (int): Posición en la serie de Fibonacci
    
    Returns:
        int: Valor de Fibonacci en la posición n
    """
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def ejercicio2():
    """
    Muestra la serie de Fibonacci hasta la posición que el usuario especifique.
    """
    print("\n" + "="*60)
    print("EJERCICIO 2: Serie de Fibonacci")
    print("="*60)
    
    try:
        posicion = int(input("Ingrese la posición hasta donde mostrar la serie: "))
        
        if posicion < 0:
            print("Error: Debe ingresar un número mayor o igual a 0")
            return
        
        print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
        print("-" * 40)
        
        for i in range(posicion + 1):
            valor = fibonacci(i)
            print(f"Posición {i}: {valor}")
            
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


# ============================================================================
# EJERCICIO 3: Potencia recursiva
# ============================================================================

def potencia(base, exponente):
    """
    Calcula la potencia de un número de forma recursiva.
    Fórmula: n^m = n * n^(m-1)
    
    Args:
        base (int/float): Número base
        exponente (int): Exponente
    
    Returns:
        int/float: Resultado de base^exponente
    """
    # Caso base
    if exponente == 0:
        return 1
    # Caso recursivo para exponentes positivos
    elif exponente > 0:
        return base * potencia(base, exponente - 1)
    # Caso recursivo para exponentes negativos
    else:
        return 1 / potencia(base, -exponente)


def ejercicio3():
    """
    Calcula la potencia de un número usando recursividad.
    """
    print("\n" + "="*60)
    print("EJERCICIO 3: Potencia recursiva")
    print("="*60)
    
    try:
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        
        resultado = potencia(base, exponente)
        print(f"\n{base}^{exponente} = {resultado}")
        
    except ValueError:
        print("Error: Debe ingresar números válidos")


# ============================================================================
# EJERCICIO 4: Conversión decimal a binario
# ============================================================================

def decimal_a_binario(n):
    """
    Convierte un número decimal a binario de forma recursiva.
    
    Args:
        n (int): Número decimal entero positivo
    
    Returns:
        str: Representación binaria del número
    """
    # Caso base
    if n == 0:
        return ""
    # Caso recursivo
    else:
        # Dividir por 2 y guardar el resto
        return decimal_a_binario(n // 2) + str(n % 2)


def ejercicio4():
    """
    Convierte un número decimal a binario usando recursividad.
    """
    print("\n" + "="*60)
    print("EJERCICIO 4: Conversión decimal a binario")
    print("="*60)
    
    try:
        numero = int(input("Ingrese un número decimal entero positivo: "))
        
        if numero < 0:
            print("Error: Debe ingresar un número positivo")
            return
        
        if numero == 0:
            binario = "0"
        else:
            binario = decimal_a_binario(numero)
        
        print(f"\nEl número {numero} en binario es: {binario}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


# ============================================================================
# EJERCICIO 5: Verificar palíndromo
# ============================================================================

def es_palindromo(palabra):
    """
    Verifica si una palabra es palíndromo de forma recursiva.
    
    Args:
        palabra (str): Palabra a verificar (sin espacios ni tildes)
    
    Returns:
        bool: True si es palíndromo, False en caso contrario
    """
    # Convertir a minúsculas para comparar
    palabra = palabra.lower()
    
    # Casos base
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo: comparar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    else:
        # Llamada recursiva con la palabra sin los extremos
        return es_palindromo(palabra[1:-1])


def ejercicio5():
    """
    Verifica si una palabra es palíndromo.
    """
    print("\n" + "="*60)
    print("EJERCICIO 5: Verificar palíndromo")
    print("="*60)
    
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    
    if es_palindromo(palabra):
        print(f"\n'{palabra}' ES un palíndromo")
    else:
        print(f"\n'{palabra}' NO es un palíndromo")


# ============================================================================
# EJERCICIO 6: Suma de dígitos
# ============================================================================

def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número de forma recursiva.
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: Suma de los dígitos
    """
    # Caso base
    if n < 10:
        return n
    # Caso recursivo
    else:
        # Sumar el último dígito (n % 10) + suma de los demás (n // 10)
        return (n % 10) + suma_digitos(n // 10)


def ejercicio6():
    """
    Calcula la suma de los dígitos de un número.
    """
    print("\n" + "="*60)
    print("EJERCICIO 6: Suma de dígitos")
    print("="*60)
    
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        if numero < 0:
            print("Error: Debe ingresar un número positivo")
            return
        
        resultado = suma_digitos(numero)
        print(f"\nLa suma de los dígitos de {numero} es: {resultado}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


# ============================================================================
# EJERCICIO 7: Contar bloques de pirámide
# ============================================================================

def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide.
    
    Args:
        n (int): Número de bloques en el nivel más bajo
    
    Returns:
        int: Total de bloques necesarios
    """
    # Caso base
    if n == 1:
        return 1
    # Caso recursivo
    else:
        return n + contar_bloques(n - 1)


def ejercicio7():
    """
    Calcula cuántos bloques se necesitan para construir una pirámide.
    """
    print("\n" + "="*60)
    print("EJERCICIO 7: Bloques de pirámide")
    print("="*60)
    
    try:
        bloques_base = int(input("Ingrese el número de bloques en la base: "))
        
        if bloques_base < 1:
            print("Error: Debe ingresar un número mayor o igual a 1")
            return
        
        total = contar_bloques(bloques_base)
        print(f"\nPara una pirámide con {bloques_base} bloques en la base")
        print(f"se necesitan {total} bloques en total")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


# ============================================================================
# EJERCICIO 8: Contar ocurrencias de un dígito
# ============================================================================

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito en un número de forma recursiva.
    
    Args:
        numero (int): Número entero positivo
        digito (int): Dígito a buscar (0-9)
    
    Returns:
        int: Cantidad de veces que aparece el dígito
    """
    # Caso base
    if numero == 0:
        return 0
    
    # Caso recursivo
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    # Si el último dígito coincide, sumar 1
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return contar_digito(resto_numero, digito)


def ejercicio8():
    """
    Cuenta cuántas veces aparece un dígito en un número.
    """
    print("\n" + "="*60)
    print("EJERCICIO 8: Contar dígito en un número")
    print("="*60)
    
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese el dígito a buscar (0-9): "))
        
        if numero < 0:
            print("Error: Debe ingresar un número positivo")
            return
        
        if digito < 0 or digito > 9:
            print("Error: El dígito debe estar entre 0 y 9")
            return
        
        cantidad = contar_digito(numero, digito)
        print(f"\nEl dígito {digito} aparece {cantidad} veces en {numero}")
        
    except ValueError:
        print("Error: Debe ingresar números enteros válidos")


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def mostrar_menu():
    """
    Muestra el menú de opciones del trabajo práctico.
    """
    print("\n" + "="*60)
    print("TP7 - RECURSIVIDAD")
    print("="*60)
    print("1. Factorial de un número")
    print("2. Serie de Fibonacci")
    print("3. Potencia recursiva")
    print("4. Conversión decimal a binario")
    print("5. Verificar palíndromo")
    print("6. Suma de dígitos")
    print("7. Bloques de pirámide")
    print("8. Contar dígito en un número")
    print("0. Salir")
    print("="*60)


def main():
    """
    Función principal del programa.
    """
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                ejercicio1()
            elif opcion == "2":
                ejercicio2()
            elif opcion == "3":
                ejercicio3()
            elif opcion == "4":
                ejercicio4()
            elif opcion == "5":
                ejercicio5()
            elif opcion == "6":
                ejercicio6()
            elif opcion == "7":
                ejercicio7()
            elif opcion == "8":
                ejercicio8()
            elif opcion == "0":
                print("\n¡Hasta luego!")
                break
            else:
                print("\nOpción inválida. Por favor, seleccione una opción del menú.")
                
            input("\nPresione ENTER para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break


# Ejecutar el programa
if __name__ == "__main__":
    main()
