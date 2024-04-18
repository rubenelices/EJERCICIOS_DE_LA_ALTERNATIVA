class Alumno:
    def __init__(self, notas):
        self.notas = notas
        self.media = sum(notas) / len(notas)
        self.evaluacion = self.calcular_evaluacion()

    def calcular_evaluacion(self):
        # Determinar la evaluación basada en la media de las notas
        if self.media > 15:
            return "Alumno con talento"
        elif 12 <= self.media <= 15:
            return "Con capacidad"
        else:
            return "Debe reorientarse"

# Solicitar al usuario que ingrese las cuatro notas del alumno
notas_alumno = []
for i in range(1, 5):
    nota = float(input(f"Ingrese la nota {i} (de 0 a 20): "))
    notas_alumno.append(nota)

# Crear una instancia de Alumno con las notas ingresadas
alumno = Alumno(notas_alumno)

# Imprimir los resultados
print(f"La media de las notas es: {alumno.media:.2f}")
print(f"Evaluación del alumno: {alumno.evaluacion}")
