# Escriba un programa que pida al usuario dos palabras, 
# y que indique cuál de ellas es la más larga y por cuántas letras lo es.
palabra1 = input('escribe una palabra: ')
palabra2 = input('escribe otra palabra: ')

def contarCaracteres(palabra):
    cantidadCaracteres = 0
    for i in palabra:
        cantidadCaracteres += 1
    return cantidadCaracteres

cantidadCaracteresPalabra1 = contarCaracteres(palabra1)
cantidadCaracteresPalabra2 = contarCaracteres(palabra2)

if cantidadCaracteresPalabra1 >= cantidadCaracteresPalabra2:
    print('La palabra', palabra1, 'es más larga que la palabra', palabra2, 'por', cantidadCaracteresPalabra1 - cantidadCaracteresPalabra2, 'caracteres')
else:
    print('La palabra', palabra2, 'es más larga que la palabra', palabra1, 'por', cantidadCaracteresPalabra2 - cantidadCaracteresPalabra1, 'caracteres')
