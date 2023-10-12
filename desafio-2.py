#Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
#numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
#desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
#pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
#desplazarse:
#Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
#una torre, e indique cuál pieza captura a la otra:

def declararUbicaciones():
    columnaAlfil = int(input('Escriba en qué columna se encuentra el alfil: '))
    filaAlfil = int(input('Escriba en qué fila se encuentra el alfil: '))

    columnaTorre = int(input('Escriba en qué columna se encuentra la torre: '))
    filaTorre = int(input('Escriba en qué fila se encuentra la torre: '))

while columnaAlfil < 1 or columnaAlfil > 8 or filaAlfil < 1 or filaAlfil > 8 or columnaTorre < 1 or columnaTorre > 8 or filaAlfil < 1 or filaAlfil > 8:
    print('Alguna de las coordenadas no fue correcta... Reintentando \n')
    declararUbicaciones()