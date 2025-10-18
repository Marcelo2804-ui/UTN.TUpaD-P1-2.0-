"""Chequeo rápido no interactivo para el TP.
Ejecuta carga y algunas operaciones clave para verificar que todo funciona.
"""
from io_utils import get_csv_path, cargar_datos
from operaciones import (
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    ordenar_paises,
    calcular_densidad,
)


def main():
    csv_path = get_csv_path("paises.csv")
    print(f"Usando CSV: {csv_path}")
    paises = cargar_datos(csv_path)
    assert paises, "No se cargaron países"

    # Buscar país parcial
    res = buscar_pais(paises, "ar")  # debería encontrar Argentina u otros
    print(f"Buscar 'ar' -> {len(res)} resultados")

    # Filtrar por continente
    res_c = filtrar_por_continente(paises, "America")
    print(f"America -> {len(res_c)} países")

    # Rango de población
    res_p = filtrar_por_poblacion(paises, 1_000_000, 200_000_000)
    print(f"Población 1M-200M -> {len(res_p)} países")

    # Ordenar por densidad
    orden = ordenar_paises(paises, "densidad", descendente=True)
    top = orden[:3]
    print("Top 3 por densidad:")
    for p in top:
        print(p['nombre'], f"{calcular_densidad(p):.2f}")


if __name__ == "__main__":
    main()
