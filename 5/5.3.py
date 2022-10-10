palabra = input("Introduce una palabra: ")
palabraReversa = palabra
palabra = list(palabra)
palabraReversa = list(palabraReversa)
palabraReversa.reverse()
if palabra == palabraReversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")