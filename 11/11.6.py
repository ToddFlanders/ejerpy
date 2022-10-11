class clientes:
    def __init__(self):
        self.nombre = input("Nombre del cliente: ")
        self.total = int(input("Inserta la cantidad: "))
    def depositar(self, ingresar):
        self.total = self.total + int(ingresar)
    def extraer(self, extraccion):
        self.total = self.total - int(extraccion)
    
    def mostrar_total(self):
        print(f"El saldo total de la cuenta actualmente: {self.total}")