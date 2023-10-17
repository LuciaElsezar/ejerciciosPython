import string

jugador1 = ''
jugador2 = ''
puntajeJugador1 = 0
puntajeJugador2 = 0

while puntajeJugador1 < 3 and puntajeJugador2 < 3:
    jugador1 = input('Jugador 1, elige Piedra, Papel o Tijera: ')
    jugador2 = input('Jugador 2, elige Piedra, Papel o Tijera: ')
    jugador1 = jugador1.lower()
    jugador2 = jugador2.lower()

    if jugador1 == 'piedra' and jugador2 == 'piedra':
        print('Ambos escogieron piedra, no hay punto para ninguno.')              
    elif jugador1 == 'piedra' and jugador2 == 'papel':
        print('Punto para Jugador 2')
        puntajeJugador2 += 1        
    elif jugador1 == 'piedra' and jugador2 == 'tijera':
        print('Punto para jugador 1')
        puntajeJugador1 += 1    
    elif jugador1 == 'papel' and jugador2 == 'piedra':
        print('Punto para jugador 1')
        puntajeJugador1 += 1        
    elif jugador1 == 'papel' and jugador2 == 'papel':
        print('Ambos escogieron papel, no hay punto para ninguno.')
    elif jugador1 == 'papel' and jugador2 == 'tijera':
        print('Punto para Jugador 2')
        puntajeJugador2 += 1
    elif jugador1 == 'tijera' and jugador2 == 'piedra':
        print('Punto para Jugador 2')
        puntajeJugador2 += 1
    elif jugador1 == 'tijera' and jugador2 == 'papel':
        print('Punto para jugador 1')
        puntajeJugador1 += 1
    elif jugador1 == 'tijera' and jugador2 == 'tijera':
        print('Ambos escogieron tijeras, no hay punto para ninguno.')
    else:
        print('Intento no valido. Nuevo intento...')
    
    print('\n Puntaje >> ', puntajeJugador1, '-', puntajeJugador2, '\n')

if puntajeJugador1 > puntajeJugador2:
    print('Ganó el Jugador 1 >>', puntajeJugador1, 'a', puntajeJugador2)
elif puntajeJugador1 < puntajeJugador2:
    print('Ganó el Jugador 2 >>', puntajeJugador1, 'a', puntajeJugador2)