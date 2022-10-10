class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mueve(self, orden):
        if orden == "A":
            miRobot.posicion_actual(self.x,self.y+1)
        if orden == "R":
            miRobot.posicion_actual(self.x,self.y-1)
        if orden == "I":
            miRobot.posicion_actual(self.x-1,self.y)
        if orden == "D":
                miRobot.posicion_actual(self.x+1,self.y)
        
    def posicion_actual(self, x, y):
        self.x = x
        self.y = y
        print("coordenadas "+ str(x)+ ","+str(y))

    """ def mueve(self, orden):
        if orden == "A":
            self.y+= 1
            miRobot.posicion_actual()
        if orden == "R":
            self.y-= 1
            miRobot.posicion_actual()
        if orden == "I":
            self.x-= 1
            miRobot.posicion_actual()
        if orden == "D":
            self.x+= 1
                miRobot.posicion_actual()
        
    def posicion_actual(self):
        print("coordenadas "+ str(self.x)+ ","+str(self.y)"""

miRobot = Robot(0,0)
orden='A'
while orden != "Fin":
    orden = input("Introduce una orden: ")
    miRobot.mueve(orden)

