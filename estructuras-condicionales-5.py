import string 

caracterIngresado = input('ingresa un caracter: ')

def contarCaracteres(palabra):
    i = 0
    for i in palabra:
        i += 1
    return i

if contarCaracteres(caracterIngresado) == 1:
    if string.ascii_lowercase.find(caracterIngresado) >= 0:
        print('El caracter',caracterIngresado, 'es una letra minúscula')
    elif string.ascii_uppercase.find(caracterIngresado) >= 0:
        print('El caracter',caracterIngresado, 'es una letra mayúscula')
    elif string.digits.find(caracterIngresado) >= 0:
        print('El caracter',caracterIngresado, 'es un número')
    elif string.punctuation.find(caracterIngresado) >= 0:
        print('El caracter',caracterIngresado, 'es un síbolo')
    else:
        print('pusiste cualquier cosa ._.')
elif contarCaracteres(caracterIngresado) > 1:
    print('Ingresar solo un caracter')
else:
    print('Ingresar al menos un caracter')