def calcular_descuento(precio, num_ninos):
    # Determinar el porcentaje de descuento según la cantidad de niños
    if num_ninos == 2:
        porcentaje_descuento = 10
    elif num_ninos == 3:
        porcentaje_descuento = 15
    elif num_ninos >= 4:
        porcentaje_descuento = 18 + (num_ninos - 4)
    else:
        porcentaje_descuento = 0  # No descuento si hay menos de 2 niños
    
    # Calcular el importe del descuento
    importe_descuento = (precio * porcentaje_descuento) / 100
    return importe_descuento

# Solicitar al usuario el precio total de los boletos y el número de niños
precio_boletos = float(input("Ingrese el precio total de los boletos: "))
numero_niños = int(input("Ingrese el número de niños: "))

# Calcular el descuento
descuento_aplicado = calcular_descuento(precio_boletos, numero_niños)

# Imprimir el resultado del descuento
print(f"El descuento aplicado es de {descuento_aplicado:.2f} euros.")

print("Por tanto el precio total de sus entradas es de:",precio_boletos-descuento_aplicado,"euros")