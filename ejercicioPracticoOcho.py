# Ejercicio práctico número ocho

# Crear diccionario vacío
productos = {}

while True:
    # Pedir nombre del producto
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    
    if nombre.lower() == "fin":
        break  # Salir del bucle si el usuario escribe 'fin'
    
    # Pedir precio del producto
    precio = float(input(f"Ingrese el precio de '{nombre}': "))
    
    # Agregar producto al diccionario
    productos[nombre] = precio
    
    # Mostrar contenido actual del diccionario
    claves = list(productos.keys())
    for i in range(len(claves)):
        clave = claves[i]
        print(f"- {clave}: ${productos[clave]}")
    print()
    
print("¡Lista de productos finalizada!")
print(productos)