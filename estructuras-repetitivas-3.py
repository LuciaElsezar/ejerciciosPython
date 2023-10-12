# Escriba un programa que pida al usuario dos números enteros, 
# y luego entregue la suma de todos los números que están entre ellos. 
# Por ejemplo, si los números son 1 y 7, 
# debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

nro1 = int(input('Escribe un número: '))
nro2 = int(input('Escribe otro número: '))
suma = 0

if nro1 <= nro2:
    for i in range(nro1+1, nro2):
        suma += i
else: 
    for i in range(nro2+1, nro1):
        suma += i

print('La suma de los números entre el', nro1, 'y el', nro2, 'da como resultado:', suma)