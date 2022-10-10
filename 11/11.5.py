class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def sumar(self):
        print("La suma es  " + str(self.n1 + self.n2))
    def restar(self):
        print("La resta es " + str(self.n1 - self.n2))
    def multiplicar(self):
        print("La multiplicación es " + str(self.n1 * self.n2))
    def division(self):
        print("La división es " + str(self.n1 / self.n2))
n1 = int(input("Inserte un número: "))
n2 = int(input("Inserte otro número: "))
c1 = Calculadora(n1, n2)
c1.sumar()
c1.restar()
c1.multiplicar()
c1.division()