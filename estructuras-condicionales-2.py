# Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año.
ano = int(input('Escribe un año: '))

if ano % 4 == 0:
    if ano <= 1582:
        print('El año', ano, 'es bisiesto.')
    else:
        if ano % 400 != 0 and ano % 100 == 0:
            print('El año', ano, 'no es bisiesto.')
        else: print('El año', ano, 'es bisiesto')
else:
    print('El año', ano, 'no es bisiesto')
