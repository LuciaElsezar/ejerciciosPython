from Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, posicionX = 0, posicionY = 0, nombre = "___", danio = 1, ataque = 1):
        self.danio = danio
        self.ataque = ataque
        super().__init__(posicionX, posicionY, nombre)

    def atacar(self, ataque = 1):
        return "El enemigo " + str(self.nombre) + " usa su ataque y hace " + str(self.danio) + " de daño"
    
# goomba = Enemigo(nombre="Goomba", danio= 3)
# print(goomba.atacar())