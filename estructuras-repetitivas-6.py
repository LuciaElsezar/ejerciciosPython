# Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario

altura = int(input('Escribe una altura: '))
str = ''

for i in range(0, altura):
    str += '*'
    print(str)