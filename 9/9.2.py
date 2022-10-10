from datetime import date
def calcular_edad(fechaNacimientoSplit):
    fechaActual = date.today()
    día = int(fechaNacimientoSplit[2])
    mes = int(fechaNacimientoSplit[1])
    año = int(fechaNacimientoSplit[0])
    edad = fechaActual.year - año -  ((fechaActual.month, fechaActual.day) < (mes, día))
    if edad >= 18:
        print(f"Eres mayor de edad: {edad} años")
    else:
        print(f"Eres menor de edad: {edad} años")

fechaNacimiento = input("dame tu fecha de nacimiento en formato aaaa/mm/dd: ")
fechaNacimientoSplit = fechaNacimiento.split("/")
calcular_edad(fechaNacimientoSplit)