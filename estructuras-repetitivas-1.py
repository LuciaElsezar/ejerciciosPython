# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#  pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
# Al final debe mostrar el nro de intentos.

contrasena = 'contraseña123'
inpt = ''
i = 0

while inpt != contrasena:
    inpt = input('Escribe la contraseña: ')
    i+=1
    if inpt != contrasena: 
        print('La contraseña no es', inpt)

print('Luego de', i, 'intentos, la contraseña si es', contrasena)