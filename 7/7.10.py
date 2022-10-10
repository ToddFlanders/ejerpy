def palindromo(oracion):
    oracion =''.join(oracion.split())
    print(oracion.split)
    print(oracion)
    i = 0
    f = len(oracion) - 1
    while oracion[i] == oracion[f]:
        if i >= f:
            return True
        i += 1
        f -= 1
    return False
oracion = input("Introduce una frase para ver si es palindroma: ")
print(palindromo(oracion))