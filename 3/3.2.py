nombre = input("Como te llamas? ")
genero = input("Cual es tu sexo (H o M)? ")
if (genero == "M" and  nombre.lower()< "m") or (genero == "H" and  nombre.lower()> "n"):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es "+ grupo)