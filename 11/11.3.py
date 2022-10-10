class Coches:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina
    def avanzar(self,kilometros):
        kilometrosRecorridos = float(self.kilometros_recorridos + kilometros)
        precioGasolina = float(self.gasolina -((self.kilometros_recorridos + kilometros)* 0.1))
        print("Los kilometros recorridos son  " + str(kilometrosRecorridos) + "km")
        if precioGasolina <= 0:
            c1.repostar(precioGasolina)
        else:
            print("Precio de la gasolina es " + precioGasolina + "€")
    def repostar(self, gasolina):
        print("Es necesario repostar para recorrer la cantidad indicada de kilómetros")
        litros = float(input("Inserte un número de litros a repostar: ")) 
        totalGasolina = litros + gasolina
        c1.gasolina = totalGasolina
        print("Gasolina actual es: " + str(c1.gasolina) + "l")


kilometros = int(input("Inserte un número de kilometros: "))
c1 = Coches("1995FHN", "Audi", float(1500), float(0))
c1.avanzar(kilometros)
