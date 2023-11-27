class Personaje:
    def __init__(self, posicionX = 0, posicionY = 0, nombre = "___"):
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY

    def mover(self, posicionX = 0):
        return self.nombre + " camina"

    def saltar(self, posicionY = 0):
        return self.nombre + " salta"

    def caer(self, posicionY = 0):
        return self.nombre + " cae"