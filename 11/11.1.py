class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

al= Alumno("Oier", 10)

if (al.nota >= 5) and (al.nota<= 10):
    print(al.nombre + " has aprobado con un " + str(al.nota))
else:
    print(al.nombre + " has suspendido con un " + str(al.nota))