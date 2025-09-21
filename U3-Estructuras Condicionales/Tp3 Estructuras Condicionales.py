# Ejercicio 5
usuario = input("Por favor, ingrese su usuario (en su primer ingreso es su nombre y apellido todo junto): ").lower()
if 8 <= len(usuario) <= 14:
    print("Ha ingresado un usuario válido")
else:
    print("Por favor, ingrese un usuario de entre 8 y 14 caracteres")

contrasena = input("Por favor, ingrese su contraseña (mínimo 8 caracteres), caso sea su primer ingreso la misma será 'marceloaprobo': ")
if contrasena == "marceloaprobo":
    print("Ha ingresado una contraseña válida")
else:
    print("Por favor, ingrese la contraseña correcta (pista: empieza con 'marcelo' y termina con 'aprobo')")

# Ejercicio 1 y 4
edad = int(input("Buenas, ¿me dirías tu edad? "))
if edad < 0:
    print("¿Edad negativa? ¿Eres un viajero del tiempo o Benjamin Button?")
elif edad < 12:
    print("Eres un niño/a, disfruta tu infancia (y los dibujitos)")
elif edad < 18:
    print("Eres un adolescente, por favor no te olvides de estudiar (y de dormir mucho)")
elif edad < 30:
    print("¡Estás en tu mejor momento! Aprovecha la vida al máximo (y no te olvides de tomar agua)")
elif edad < 65:
    print("Tienes entre 30 y 65 años, eres un adulto en plenitud (o sobreviviendo a la adultez)")
else:
    print("Eres un anciano/a, guerrero/a de la vida. ¡Aplausos por llegar hasta acá!")

# Ejercicio 2
nota = float(input("Ingrese la última nota que recuerdes: "))
if nota >= 6:
    print("¡Bien ahí! Aprobaste, sigue así.")
else:
    print("¡Reprobaste! Como decía mi abuela: faltó perseverancia xD")

# Ejercicio 3
if edad % 2 == 0:
    print("Aca razonando en datos inútiles me di cuenta que tu edad es par, xD")
else:
    print("Aca razonando en datos inútiles me di cuenta que tu edad es impar, que loco no?")

# Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("\nNúmeros generados:")
print(numeros_aleatorios)

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("\nEstadísticas:")
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("\nSesgo positivo o a la derecha")
elif media < mediana < moda:
    print("\nSesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("\nSin sesgo")
else:
    print("\nNo se puede determinar si esta distribución tiene sesgo o no")

# Ejercicio 7
lista_numeros = [5, 12, 23, 34, 45]
numero = int(input("\nEjercicio 7: Ingrese un número para ver si está en la lista mágica: "))
if numero in lista_numeros:
    print("¡Sí! El número está en la lista. Sos parte del club secreto 🕵️‍♂️")
else:
    print("No está en la lista... pero podés crear tu propia 😎")

# Ejercicio 8
print("\nEjercicio 8: Mostrando los elementos de la lista uno por uno:")
for elemento in lista_numeros:
    print("Elemento:", elemento)

# Ejercicio 9
print("\nEjercicio 9: Contando los elementos de la lista:")
print("La lista tiene", len(lista_numeros), "elementos. No está mal para empezar.")

# Ejercicio 10
print("\nEjercicio 10: Vamos a crear una lista personalizada.")
mi_lista = []
for i in range(3):
    dato = input(f"Ingrese el dato número {i+1}: ")
    mi_lista.append(dato)

print("Tu lista personalizada quedó así:", mi_lista)


#Profe del 6 al 10 se me termino las ideas, la aplicacion de lista debo practicarla mas.