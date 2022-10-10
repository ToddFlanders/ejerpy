print("cuantos payasos se han vendido en el utlimo pedido?")
payaso = int(input())
payasotot= payaso * 112
print("cuantas muñecas se han vendido en el utlimo pedido?")
muñeca = int(input())
muñecatot= muñeca * 75
total = payasotot + muñecatot
print(f"El peso total del paquete es {total} g")