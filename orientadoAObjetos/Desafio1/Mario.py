from Personaje import Personaje

class Mario(Personaje):
    def __init__(self, nombre = "Mario", posicionX = 0, posicionY = 0, vidas = 3):
        self.vidas = vidas
        super().__init__(posicionX, posicionY, nombre)

    def lanzarFuego(self, bolaFuego = 0):
        return self.nombre + " lanza una bola de fuego"

# mario = Mario()
# print(mario.lanzarFuego())
        