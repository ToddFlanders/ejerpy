import datetime
"""fecha = input("Cual est tu fecha de nacimiento en formato dd/mm/aa? ")
fechaSplit = fecha.split("/")
día = int(fechaSplit[2])
mes = int(fechaSplit[1])
año = int(fechaSplit[0])
x = datetime.date(año,mes,día)
print(x.strftime("%A"))"""


año = input("introduce un año: ")
fecha = input("Cual est tu fecha de nacimiento en formato dd/mm/aa? ")
fechaSplit = fecha.split("/")
cumpleañosfut = datetime.datetime(int(año), int(fechaSplit[1]), int(fechaSplit[0]))
nacimiento = datetime.datetime(int(fechaSplit[2]), int(fechaSplit[1]), int(fechaSplit[0]))
print(f"""Naciste un  {nacimiento.strftime('%A')}
y tu cumpleaños en el año {año} cae el dia {cumpleañosfut.strftime('%A')}""")

