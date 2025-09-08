# Ejercicio práctico número siete

# Creo la lista de clientes vacia
customers = []

# Cargó la lista de clientes y evaluó si estan vacios
while True:
    customer_load = input("Ingrese el nombre del cliente (escriba 'fin' para terminar): ").strip()
    
    if customer_load.lower() == "fin":   # si escribe 'fin', termina
        break
    
    if customer_load == "":   # si está vacío, aviso y no lo guardo
        print("El nombre no puede estar vacío, inténtelo de nuevo.")
        continue
    
    customers.append(customer_load)

# Implemento el método .sort() para ordenar la lista de clientes
customers.sort()

# Muestro la lista de clientes ordenada
print("\nLista de clientes ordenada:")
i = 1
for customer in customers:
    print(f"{i}. {customer}")
    i += 1