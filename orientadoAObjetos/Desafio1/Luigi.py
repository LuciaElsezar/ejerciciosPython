from Personaje import Personaje

class Luigi(Personaje):
    def __init__(self, nombre = "Luigi", posicionX = 0, posicionY = 0, vidas = 3):
        self.vidas = vidas
        super().__init__(posicionX, posicionY, nombre)

    def usarHongo(self, hongo = 0):
        return self.nombre + " utiliza un hongo"
    
# luigi = Luigi()
# print(luigi.usarHongo())
        