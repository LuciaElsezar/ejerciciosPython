from Enemigo import Enemigo

class Goomba(Enemigo):
    def __init__(self, posicionX = 0, posicionY = 0, nombre = "goomba", danio = 1, ataque = 1):
        super().__init__(posicionX, posicionY, nombre, danio, ataque)
    
    def saltar(self, posicionY = 0):
        return "El goomba " + str(self.nombre) + " ha saltado!!"
    
# goomba = Goomba(nombre="Petizo")
# print(goomba.saltar())
