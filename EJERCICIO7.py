def calcular_coste_trayecto(num_alumnos):
    if num_alumnos > 25:
        precio_trayecto = 61.00
    else:
        precio_trayecto = 67.30
    return precio_trayecto

def calcular_coste_alojamiento(num_alumnos):
    if num_alumnos < 30:
        precio_alojamiento = 4.75
    elif 30 <= num_alumnos <= 35:
        precio_alojamiento = 4.00
    else:
        precio_alojamiento = 3.50
    return precio_alojamiento

def calcular_costo_viaje(num_alumnos, num_dias):
    precio_trayecto = calcular_coste_trayecto(num_alumnos)
    precio_alojamiento = calcular_coste_alojamiento(num_alumnos)
    precio_comida = 3.50
    
    costo_por_alumno = (precio_trayecto + (precio_alojamiento + precio_comida) * num_dias)
    costo_total_viaje = costo_por_alumno * num_alumnos
    
    return costo_por_alumno, costo_total_viaje

# Solicitar al usuario la cantidad de alumnos y la duración del viaje
numero_alumnos = int(input("Ingrese la cantidad de alumnos: "))
duracion_dias = int(input("Ingrese la duración del viaje en días: "))

# Calcular el costo por alumno y el costo total del viaje
costo_alumno, costo_total = calcular_costo_viaje(numero_alumnos, duracion_dias)

# Imprimir los resultados
print(f"El costo por alumno es de {costo_alumno:.2f} euros.")
print(f"El costo total del viaje es de {costo_total:.2f} euros.")
