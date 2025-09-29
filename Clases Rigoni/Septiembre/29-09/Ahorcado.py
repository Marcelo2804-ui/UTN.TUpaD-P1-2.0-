import random

def obtener_palabra_aleatoria():
    """Elige una palabra al azar de una lista predefinida."""
    palabras = ["python", "programacion", "tecnologia", "universidad", "desarrollo"]
    return random.choice(palabras)

def mostrar_tablero(dibujo_ahorcado, letras_incorrectas, palabra_secreta, letras_adivinadas):
    """Muestra el dibujo del ahorcado, las letras incorrectas y la palabra oculta."""
    print(dibujo_ahorcado[6 - len(letras_incorrectas)])
    print()

    print("Letras incorrectas:", " ".join(letras_incorrectas))
    print()

    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    
    print(palabra_mostrada)
    print()

def jugar_ahorcado():
    """Función principal para ejecutar el juego del ahorcado."""
    DIBUJO_AHORCADO = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========''']

    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    letras_incorrectas = []
    intentos = 6
    juego_terminado = False

    while not juego_terminado:
        mostrar_tablero(DIBUJO_AHORCADO, letras_incorrectas, palabra_secreta, letras_adivinadas)

        letra_ingresada = input("Ingresa una letra: ").lower()

        if letra_ingresada in letras_adivinadas or letra_ingresada in letras_incorrectas:
            print("Ya habías ingresado esa letra. Intenta con otra.")
            continue

        if letra_ingresada in palabra_secreta:
            letras_adivinadas.append(letra_ingresada)
            print("¡Letra correcta!")
        else:
            letras_incorrectas.append(letra_ingresada)
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        # Comprobar si ganó
        ganador = True
        for letra in palabra_secreta:
            if letra not in letras_adivinadas:
                ganador = False
                break
        
        if ganador:
            print(f"¡Felicitaciones! ¡Adivinaste la palabra: {palabra_secreta}!")
            juego_terminado = True
        
        if intentos == 0:
            mostrar_tablero(DIBUJO_AHORCADO, letras_incorrectas, palabra_secreta, letras_adivinadas)
            print(f"¡Perdiste! La palabra secreta era: {palabra_secreta}")
            juego_terminado = True

# Iniciar el juego
jugar_ahorcado()