# Escriba un programa que entregue todos los divisores del número entero ingresado:

nro = int(input('Escribe un número y te diré los números que lo dividen: '))
listaNrosDivisores = []

for i in range(2, nro):
    if nro % i == 0:
        listaNrosDivisores.append(i)

print('Los números que son divisores del número', nro,'son:', listaNrosDivisores)