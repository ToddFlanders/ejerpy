persona = {}
next = True
while next :
    dato = input("Que dato deseas introducir? ")
    datoIntroducido = input(dato + ": ")
    persona[dato] = datoIntroducido
    print (persona)
    next = input('¿Quieres añadir más información (Si/No)? ') == "Si"