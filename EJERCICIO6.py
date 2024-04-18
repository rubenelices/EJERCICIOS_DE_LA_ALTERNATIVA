def calcular_descuento(cantidad, cliente):
    # Convertir el nombre del cliente a minúsculas para uniformidad
    cliente = cliente.lower()

    # Determinar el descuento base según la cantidad de componentes
    if 10000 <= cantidad <= 20000:
        descuento_base = 10
    elif 20001 <= cantidad <= 40000:
        descuento_base = 15
    elif cantidad > 40000:
        descuento_base = 20
    else:
        descuento_base = 0  # No descuento para menos de 10000 componentes

    # Ajustar el descuento según el cliente
    if cliente == "commaq":
        descuento_final = descuento_base - 2
    elif cliente == "bel":
        descuento_final = descuento_base + 1
    else:
        descuento_final = descuento_base

    # Asegurar que el descuento no caiga por debajo de 0
    descuento_final = max(descuento_final, 0)

    return descuento_final

# Solicitar al usuario que ingrese la cantidad de componentes y el nombre del cliente
cantidad_componentes = int(input("Ingrese la cantidad de microprocesadores pedidos: "))
nombre_cliente = input("Ingrese el nombre del cliente: ")

# Calcular el porcentaje de descuento
descuento_aplicado = calcular_descuento(cantidad_componentes, nombre_cliente)

# Imprimir el resultado del porcentaje de descuento
print(f"El porcentaje de descuento concedido es del {descuento_aplicado}%.")

