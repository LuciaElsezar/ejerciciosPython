from Goomba import Goomba
from KoopaTroopa import KoopaTroopa
from Luigi import Luigi
from Mario import Mario

mario = Mario(nombre = "Mario B)")
luigi = Luigi(nombre = "Luigi :D")
goomba = Goomba(nombre = "Goombita", danio = 2)
koopaTroopa = KoopaTroopa(nombre = "Koopita")

print(mario.mover())
print(mario.saltar())
print(mario.caer())
print(mario.lanzarFuego())
print(luigi.mover())
print(luigi.usarHongo())
print(goomba.mover())
print(goomba.atacar())
print(goomba.saltar())
print(koopaTroopa.caer())
print(koopaTroopa.usarCasco())
