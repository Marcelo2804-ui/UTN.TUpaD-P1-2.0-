# Ejercicio 1
print('Ejercicio 1')

multiple_4 = []

for i in range(1, 101):
    if i % 4 == 0:
        multiple_4.append(i) # agrega i a la lista

# print(multiple_4)  [El ejercicio nunca pide que se muestre]

print('')

# Ejercicio 2
print('Ejercicio 2')

list = ['Mirko', 'Lavezzi', 'Pipi', 'Insua', 'Romeo']

print(list[-2])  # el elemento 3 ó -2

print('')

# Ejercicio 3
print('Ejercicio 3')

empty_list = []

empty_list.append('casa')
empty_list.append('perro')
empty_list.append('gato')

print (empty_list)

print('')

# Ejercicio 4
print('Ejercicio 4')

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = 'loro'
animales[3] = 'oso' # no es necesario usar remove y luego insert

print(animales)

print('')

# Ejercicio 5
print('Ejercicio 5')

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Lo que hace el ejercicio es remover con el .remove el maximo numero de la lista numeros, (en este caso el 22)

print('')

# Ejercicio 6
print('Ejercicio 6')

number_list = []

for i in range(10, 31, 5): # number_list = list(range(10, 31, 5))
    number_list.append(i)

print(number_list[:2])
    

print('')

# Ejercicio 7
print('Ejercicio 7')

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = 'Corsita'
autos[2] = 'Audi'

# print (autos)

print('')

# Ejercicio 8
print('Ejercicio 8')

dobles = []

for i in range(5, 16, 5):
    i *= 2
    dobles.append(i)

print(dobles)

print('')

# Ejercicio 9
print('Ejercicio 9')

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# cliente 1: pan / leche
# cliente 2: arroz / fideos / salsa
# cliente 3: agua

compras[2].append('jugo')
compras[1][1] = 'tallarines'
compras[0].remove('pan')

print(compras)

print('')

# Ejercicio 10
print('Ejercicio 10')

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print (lista_anidada)

print('')