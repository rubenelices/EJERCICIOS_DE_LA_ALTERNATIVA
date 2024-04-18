def calcular_prima_distancia(kilometros):
    prima_distancia = min(0.01 * kilometros, 400)
    return prima_distancia

def calcular_prima_antiguedad(años_antiguedad):
    if años_antiguedad < 4:
        prima_antiguedad = 0
    else:
        prima_antiguedad = 200 + 20 * (años_antiguedad - 4)
    return prima_antiguedad

def ajustar_prima_por_accidentes(prima_total, num_accidentes):
    if num_accidentes == 1:
        prima_ajustada = prima_total * 0.5
    elif num_accidentes == 2:
        prima_ajustada = prima_total * (1/3)
    elif num_accidentes == 3:
        prima_ajustada = prima_total * 0.25
    elif num_accidentes > 3:
        prima_ajustada = 0
    else:
        prima_ajustada = prima_total
    return prima_ajustada

def calcular_prima_anual(kilometros, años_antiguedad, num_accidentes):
    prima_distancia = calcular_prima_distancia(kilometros)
    prima_antiguedad = calcular_prima_antiguedad(años_antiguedad)
    prima_total = prima_distancia + prima_antiguedad
    prima_final = ajustar_prima_por_accidentes(prima_total, num_accidentes)
    return prima_final

# Solicitar al usuario los datos necesarios
kilometros_recorridos = float(input("Ingrese el total de kilómetros recorridos por el año: "))
años_antiguedad = int(input("Ingrese los años de antigüedad del conductor: "))
num_accidentes = int(input("Ingrese el número de accidentes con responsabilidad > 20%: "))

# Calcular la prima anual
prima_anual = calcular_prima_anual(kilometros_recorridos, años_antiguedad, num_accidentes)

# Imprimir el resultado de la prima anual
print(f"La prima anual que se concederá al conductor es de {prima_anual:.2f} euros.")
