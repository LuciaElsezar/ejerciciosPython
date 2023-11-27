from Enemigo import Enemigo

class KoopaTroopa(Enemigo):
    def __init__(self, posicionX = 0, posicionY = 0, nombre = "Koopa", danio = 2, ataque = 2):
        super().__init__(posicionX, posicionY, nombre, danio, ataque)

    def usarCasco(self, casco = 0):
        return "El koopa troopa " + str(self.nombre) + " ahora usa su casco"
    
# koopaTroopa = KoopaTroopa()
# print(koopaTroopa.usarCasco())