def leer_productos():
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("El archivo no existe. Creando uno nuevo...")
        open("productos.txt", "w").close()
    return productos

def mostrar_productos(productos):
    for p in productos:
        print(f"Producto: {p['nombre']}\nPrecio: ${p['precio']}\nCantidad: {p['cantidad']}\n")

def agregar_producto(productos):
    nombre = input("Ingrese nombre: ")
    precio = float(input("Ingrese precio: "))
    cantidad = int(input("Ingrese cantidad: "))
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

def buscar_producto(productos):
    nombre = input("Ingrese el nombre a buscar: ")
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {p}")
            return
    print("Producto no encontrado.")

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

# Programa principal
productos = leer_productos()
mostrar_productos(productos)
agregar_producto(productos)
buscar_producto(productos)
guardar_productos(productos)