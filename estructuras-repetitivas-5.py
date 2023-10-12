# Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo 
# y lo dibuje utilizando asteriscos:

ancho = int(input('Escribe un ancho: '))
altura = int(input('Escribe una altura: '))
str = ''
for i in range(0,ancho):
    str += '*'
for i in range(0, altura):
    print(str)