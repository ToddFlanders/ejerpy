
def multiplicacionnumero(numero):
    for i in range(11):
        print (numero, "*", i, "=", numero*i)

numero = int(input("Introduce número: "))
multiplicacionnumero(numero)