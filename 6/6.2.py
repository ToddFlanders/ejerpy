mes = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio, 8:agosto", 9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}
fechaSplit = input("Introduce una fecha en formato dd/mm/aaaa: ")
fechaSplit = fechaSplit.split("/")
print(fechaSplit[0], "de", mes[int(fechaSplit[1])], "de", fechaSplit[2])