# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

nro = int(input('Escribe un número y te diré si es primo o no: '))
listaNrosDivisores = []
esPrimo = True

for i in range(2, nro):
    if nro % i == 0:
        listaNrosDivisores.append(i)
        esPrimo = False

if esPrimo == True:
    print('El número',nro ,'es primo')
else:
    if len(listaNrosDivisores) == 1:
        print('El número', nro, 'no es primo, y se puede dividir por el número', listaNrosDivisores[0])
    else: 
        print('El número', nro, 'no es primo, y se puede dividir por los números', listaNrosDivisores[0:])


