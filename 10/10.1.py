def conversionGrados(c):
    f = (c * 1.8) + 32
    print (f"Los grados Celsius son {c} grados Fahrenheit, {f}")
c = float(input("Ingrese la temperatura en grados Celsius: "))
if c < 0:
    raise Exception ("Inserte números enteros")
conversionGrados(c)