"""
Módulo de utilidades para validación de entrada de datos.
Contiene funciones auxiliares para solicitar y validar datos del usuario.
"""

def preguntar_nuevamente(texto):
    """
    Solicita al usuario una respuesta de sí/no y valida la entrada.
    
    Args:
        texto: mensaje a mostrar al usuario
    
    Returns:
        True si responde "si", False si responde "no"
    """
    while True:
        pregunta = input(texto).strip().lower()
        if pregunta in ("si", "no"):
            return pregunta == "si"
        print("Respuesta inválida. Ingresar 'si' o 'no'.")


def pedir_int(msg, vacio=False):
    """
    Solicita al usuario un número entero con validación.
    
    Args:
        msg: mensaje a mostrar al usuario
        vacio: si True, permite dejar el campo vacío (retorna None)
    
    Returns:
        Número entero ingresado o None si se dejó vacío
    """
    dato = input(msg).strip()
    if vacio and dato == "":
        return None
    try:
        return int(dato)
    except:
        print("Debe ser un número entero.")
        return None


def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    Útil para permitir al usuario leer los resultados antes de continuar.
    """
    input("\nPresione ENTER para continuar...")


def menu_salida():
    """
    Muestra un menú para elegir dónde volver después de una operación.
    
    Returns:
        "submenu" para volver al submenú actual y realizar otra operación
        "principal" para volver al menú principal
    """
    while True:
        print("\n¿Qué desea hacer?")
        print("  [1] Realizar otra operación en este submenú")
        print("  [2] Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            return "submenu"
        elif opcion == "2":
            return "principal"
        else:
            print("Opción inválida. Ingrese 1 o 2.")
