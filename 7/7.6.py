"""n = ["Pedro: "1500, "Juan: "2500, "Eduardo: "1500, "Dani: "2500, "Aitor: "1200, "Eneko: "2700, "Jaine: "1600, "Markel: "2500]
print(max(n))"""


def calcularSueldo(obj):
    print(max(obj, key= obj.get))
obj = {}
for i in range(8):
    nombre = input("Introduce un nombre: ")
    sueldo = input("introduce un sueldo: ")
    obj[nombre] = sueldo
    
print("EL empleado que más gana es: ", obj)
calcularSueldo(obj)