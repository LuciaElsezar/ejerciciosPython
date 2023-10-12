# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
from decimal import *
nro = Decimal(input('Escribe un número: '))
decimal = nro - int(nro)
print('La parte decimal de ', nro, 'es: ', decimal)

