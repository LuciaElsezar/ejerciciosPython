#Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
#numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
#desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
#pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
#desplazarse:
#Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
#una torre, e indique cuál pieza captura a la otra:

# ---- > Aún sin finalizar

filaAlfil = 0
columnaAlfil = 0
filaTorre = 0
columnaTorre = 0

quienGana = ''

str = '|'

def declararColumnaAlfil():
    return int(input('--Escriba la columna en la que se encuentra el alfil: '))
def declararFilaAlfil():
    return int(input('--Escriba la fila en la que se encuentra el alfil: '))
def declararColumnaTorre():
    return int(input('--Escriba la columna en la que se encuentra la torre: '))
def declararFilaTorre():
    return int(input('--Escriba la fila en la que se encuentra la torre: '))

filaAlfil = declararFilaAlfil()
columnaAlfil = declararColumnaAlfil()
filaTorre = declararFilaTorre()
columnaTorre = declararColumnaTorre()

while filaAlfil < 1 or filaAlfil > 8 or columnaAlfil < 1 or columnaAlfil > 8:
    print('Coordenadas del alfil incorrectas. Reintentando... \n')
    filaAlfil = declararFilaAlfil()
    columnaAlfil = declararColumnaAlfil()

while filaTorre < 1 or filaTorre > 8 or columnaTorre < 1 or columnaTorre > 8:
    print('Coordenadas de la Torre incorrectas. Reintentando... \n')
    filaTorre = declararFilaTorre()
    columnaTorre = declararColumnaTorre()

while columnaTorre == columnaAlfil and filaTorre == filaAlfil:
    print('Se dio las mismas coordenadas para la torre y el alfil. Reintentando...')
    filaAlfil = declararFilaAlfil()
    columnaAlfil = declararColumnaAlfil()
    filaTorre = declararFilaTorre()
    columnaTorre = declararColumnaTorre()

print('\n---*Redoble de tambores*---')

if filaAlfil == filaTorre or columnaAlfil == columnaTorre:
    quienGana = 'Torre'
    print('La torre se come al alfil:')
elif abs(columnaAlfil - columnaTorre) == abs(filaAlfil - filaTorre):
    quienGana = 'Alfil'
    print('El alfil se come a la torre:')
else:
    quienGana = 'Empate'
    print('Ninguno se come. Es empate:')

print('   1 2 3 4 5 6 7 8')
print('   _ _ _ _ _ _ _ _')

for fila in range(1,9):
    for columna in range(1,9):
        if columnaAlfil == columna and filaAlfil == fila:
            str += 'A|'
        elif columnaTorre == columna and filaTorre == fila:
            str += 'T|'
        
        elif (filaAlfil >= fila and filaTorre <= fila) or (filaAlfil <= fila and filaTorre >= fila):
            if (columnaAlfil >= columna and columnaTorre <= columna) or (columnaAlfil <= columna and columnaTorre >= columna):
                if quienGana == 'Alfil':
                    if abs(columnaAlfil - columna) == abs(filaAlfil - fila):
                        str += '*|'
                    else:
                        str += '_|'
                elif quienGana == 'Torre':
                    if columnaTorre == columna or filaTorre == fila:
                        str += '*|'
                    else:
                        str += '_|'
                else:
                    str += '_|'
            else:
                str += '_|'
        else:
            str += '_|'
    print(fila, str)
    str = '|'