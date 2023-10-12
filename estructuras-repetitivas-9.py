# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo.

nro = int(input('Escribe un número entero: '))
string = ''

if nro % 2 == 0:
    for i in range(0,nro +2 ,2):
        string = str(i) + ' ' + string
        print (string)
else:
    for i in range(1,nro +2 ,2):
        string = str(i) + ' ' + string
        print (string)

