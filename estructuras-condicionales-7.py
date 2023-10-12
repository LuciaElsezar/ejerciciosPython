equipoA = int(input('Escriba cuántos juegos ganó A: '))
equipoB = int(input('Escriba cuántos juegos ganó B: '))
if equipoA <=7 and equipoB <=7:
    if equipoA == 7:
        if equipoB == 6 or equipoB == 5:
            print('Ganó el equipo A.')
        else:
            print('Partido no válido.')
    elif equipoB == 7:
        if equipoA == 6 or equipoA == 5:
            print('Ganó el equipo B.')
        else:
            print('Partido no válido.')
    elif equipoA == 6:
        if equipoB <= 4:
            print('Ganó el equipo A.')
        else:
            print('Aún no termina.')
    elif equipoB == 6:
        if equipoA <= 4:
            print('Ganó el equipo B.')
        else:
            print('Aún no termina.')
else:
    print('Partido no válido.')
