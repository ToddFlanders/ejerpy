asignaturas = ["Matemáticas ", "Física ", "Química ", "Historia ", "Lengua "]
notas = []
aprobadas = []
for asignatura in asignaturas:
    nota= float(input("Que nota has sacado en "+ asignatura + "? "))
    if nota >= 5:
        aprobadas.append(asignatura) 
for asignatura in aprobadas:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))