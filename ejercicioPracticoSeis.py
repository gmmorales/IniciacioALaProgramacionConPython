# Ejercicio práctico número seis

# Lista de clientes (puede contener nombres en blanco)
clientes = ["ana", "", "JUAN", "maria", "PEDRO", "", "erica"]

# Recorremos la lista a través de sus indices
for i in range(len(clientes)):
    cliente = clientes[i]
    if cliente.strip() == "":   # Si está vacío o solo espacios
        print(f"Cliente {i+1}: nombre no válido (está en blanco).")
    else:
        # Formato adecuado: primera letra mayúscula, resto minúscula
        nombre_formateado = cliente.capitalize()
        print(f"Cliente {i+1}: {nombre_formateado}")