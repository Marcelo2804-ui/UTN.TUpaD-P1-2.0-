# TP Funciones – Programación I (UTN)
# Solución simple y directa, lista para ejecutar desde consola.
# Autor: (Scherer Marcelo)
# Fecha: 2025-10-08

import math

def imprimir_hola_mundo():
    """Imprime 'Hola Mundo!'"""
    print('Hola Mundo!')

def saludar_usuario(nombre):
    """Devuelve un saludo personalizado con el nombre dado."""
    return 'Hola ' + nombre + '!'

def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime una frase con la información personal suministrada."""
    # Conversión mínima a string por si edad viene como número
    print('Soy ' + str(nombre) + ' ' + str(apellido) + ', tengo ' + str(edad) + ' años y vivo en ' + str(residencia))

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas (como número con decimales)."""
    return segundos / 3600.0

def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número del 1 al 10."""
    for i in range(1, 11):
        print(str(numero) + ' x ' + str(i) + ' = ' + str(numero * i))

def operaciones_basicas(a, b):
    """Devuelve una tupla: (suma, resta, multiplicación, división).
    Si b == 0, la división se devuelve como None para evitar error."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = (a / b) if b != 0 else None
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    """Devuelve el índice de masa corporal (IMC = peso / altura^2)."""
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3.0

def main():
    # 1) imprimir_hola_mundo
    imprimir_hola_mundo()

    # 2) saludar_usuario(nombre)
    nombre = input('Ingresá tu nombre: ')
    saludo = saludar_usuario(nombre)
    print(saludo)

    # 3) informacion_personal(nombre, apellido, edad, residencia)
    nombre2 = input('Nombre: ')
    apellido2 = input('Apellido: ')
    edad_txt = input('Edad: ')
    if edad_txt.isdigit():
        edad2 = int(edad_txt)
    else:
        edad2 = edad_txt
    residencia2 = input('Residencia: ')
    informacion_personal(nombre2, apellido2, edad2, residencia2)

    # 4) área y perímetro de círculo
    radio_txt = input('Radio del círculo (número): ')
    radio = float(radio_txt) if radio_txt.replace('.', '', 1).isdigit() else 0.0
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print('Área del círculo:', area)
    print('Perímetro del círculo:', perimetro)

    # 5) segundos a horas
    seg_txt = input('Segundos (entero): ')
    segundos = int(seg_txt) if seg_txt.isdigit() else 0
    horas = segundos_a_horas(segundos)
    print('Horas:', horas)

    # 6) tabla de multiplicar
    num_tabla_txt = input('Número para la tabla de multiplicar: ')
    numero_tabla = int(num_tabla_txt) if num_tabla_txt.lstrip('-').isdigit() else 0
    tabla_multiplicar(numero_tabla)

    # 7) operaciones básicas
    a_txt = input('a: ')
    b_txt = input('b: ')
    def _to_float(txt):
        t = txt.strip()
        if t.startswith(('+', '-')):
            t2 = t[1:]
        else:
            t2 = t
        if t2.replace('.', '', 1).isdigit():
            return float(t)
        return 0.0
    a = _to_float(a_txt)
    b = _to_float(b_txt)
    s, r, m, d = operaciones_basicas(a, b)
    print('Suma:', s)
    print('Resta:', r)
    print('Multiplicación:', m)
    print('División:', d if d is not None else 'indefinida (b no puede ser 0)')

    # 8) IMC
    peso = _to_float(input('Peso en kg: '))
    altura = _to_float(input('Altura en metros: '))
    imc = calcular_imc(peso, altura) if altura != 0 else 0
    print('IMC:', format(imc, '.2f'))

    # 9) Celsius a Fahrenheit
    c = _to_float(input('Temperatura en °C: '))
    f = celsius_a_fahrenheit(c)
    print('Fahrenheit:', f)

    # 10) Promedio de tres números
    a3 = _to_float(input('Número 1: '))
    b3 = _to_float(input('Número 2: '))
    c3 = _to_float(input('Número 3: '))
    prom = calcular_promedio(a3, b3, c3)
    print('Promedio:', prom)

if __name__ == '__main__':
    main()