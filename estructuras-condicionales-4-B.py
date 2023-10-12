# A continuación, escriba otro programa que haga lo mismo con tres números.
nro1 = int(input('Ingresa un número'))
nro2 = int(input('Ingresa otro número'))
nro3 = int(input('Ingresa otro número'))

listaNumeros = list((nro1, nro2, nro3))

listaNumeros.sort()

print(listaNumeros)