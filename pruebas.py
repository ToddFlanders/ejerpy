"""
print("Inserta tu peso")
peso = float(input())
print("Inserta tu estatura")
estatura = float(input())
imc = float(peso /((estatura * estatura) /100000))
print(f"tu imc es {imc}")

print("dime tu nombre: ")
nombre = input()
nombremayus = nombre.upper()
nombreminus = nombre.lower()
nombretitulo = nombre.title()
print(nombremayus, nombreminus, nombretitulo)

numero = input(print("dame un numero de telefono formato +34-xxxxxxxxx-xx: "))
numerosplit = numero.split("-")
print(numerosplit[1])

frase = input("Escribe una frase \n")
print(frase[::-1])
"""
n = int(input("mete un numero: "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")


"""
python flask para hacer servidor web
if __name__ == "__main__"#para importar librerias y que funcionen se utiliza pero lo que va debajo se tabula
"""