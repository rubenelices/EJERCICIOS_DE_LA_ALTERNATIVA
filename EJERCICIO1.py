from enum import Enum, auto

class DIA(Enum):
    LUNES = auto()
    MARTES = auto()
    MIERCOLES = auto()
    JUEVES = auto()
    VIERNES = auto()
    SABADO = auto()
    DOMINGO = auto()

def sucesor(dia):
    # Obtener la lista de los días en orden
    dias = list(DIA)
    
    # Encontrar el índice actual del día dado
    indice_actual = dias.index(dia)
    
    # Calcular el índice del próximo día
    indice_siguiente = (indice_actual + 1) % len(dias)
    
    # Devolver el día correspondiente al índice siguiente
    return dias[indice_siguiente]

# Solicitar al usuario que ingrese un día de la semana
dia_usuario = input("Ingrese un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ")

# Normalizar la entrada del usuario para que coincida con los nombres de la enumeración
dia_usuario = dia_usuario.upper()

try:
    # Convertir la entrada del usuario a un día de la enumeración
    dia_actual = DIA[dia_usuario]
    # Obtener el día siguiente
    dia_siguiente = sucesor(dia_actual)
    print(f"El día siguiente a {dia_actual.name.capitalize()} es {dia_siguiente.name.capitalize()}.")
except KeyError:
    print("El día ingresado no es válido. Asegúrate de escribir correctamente el día de la semana.")

