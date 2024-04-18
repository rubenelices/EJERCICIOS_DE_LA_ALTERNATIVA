def calcular_descuento(importe):
    # Comprobar el rango del importe y aplicar el descuento correspondiente
    if importe >= 100 and importe <= 500:
        descuento = importe * 0.05
    elif importe > 500:
        descuento = importe * 0.08
    else:
        descuento = 0

    return descuento

# Solicitar al usuario que ingrese el importe de la compra
importe_compra = float(input("Ingrese el importe de la compra: "))

# Calcular el descuento
descuento_aplicado = calcular_descuento(importe_compra)

print(f"El descuento aplicado es de {descuento_aplicado:.2f} euros.")
print("Por tanto su compra se queda en: ",importe_compra-descuento_aplicado,"euros") 