# Escriba un programa que reciba como entrada dos números, 
# y los muestre ordenados de menor a mayor
nro1 = int(input('Ingresa un número'))
nro2 = int(input('Ingresa otro número'))

listaNumeros = list((nro1, nro2))

listaNumeros.sort()

print(listaNumeros)