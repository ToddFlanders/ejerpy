monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Inserte una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))