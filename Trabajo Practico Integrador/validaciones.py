from typing import Optional


def pedir_entero(prompt: str, minimo: Optional[int] = None, maximo: Optional[int] = None) -> int:
    """Pide un entero por consola con validaciones y mensajes claros."""
    while True:
        valor_str = input(prompt).strip()
        try:
            valor = int(valor_str)
        except ValueError:
            print("✗ Debe ingresar un número entero válido")
            continue
        if minimo is not None and valor < minimo:
            print(f"✗ El valor debe ser ≥ {minimo}")
            continue
        if maximo is not None and valor > maximo:
            print(f"✗ El valor debe ser ≤ {maximo}")
            continue
        return valor


def pedir_texto(prompt: str, permitir_vacio: bool = False) -> str:
    """Pide un texto no vacío salvo que se permita vacío."""
    while True:
        texto = input(prompt).strip()
        if texto or permitir_vacio:
            return texto
        print("✗ Debe ingresar un texto válido")
