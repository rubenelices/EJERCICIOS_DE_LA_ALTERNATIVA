# Definir la función para clasificar dos números basándose en su suma y producto
def classify_numbers(a, b):
    # Calcular el producto y la suma
    product = a * b
    sum_ab = a + b

    # Crear una lista de los valores
    values = [a, b, product, sum_ab]

    # Ordenar la lista de menor a mayor
    sorted_values = sorted(values)

    # Retornar la lista ordenada
    return sorted_values

# Solicitar al usuario que ingrese los números
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Usar la función con los números ingresados
result = classify_numbers(a, b)

# Imprimir los resultados
print("Los valores clasificados son:", result)
