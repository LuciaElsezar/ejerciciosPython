# La secuencia de Collatz de un número entero se construye de la siguiente forma:

# si el número es par, se lo divide por dos;
# si es impar, se le multiplica tres y se le suma uno;
# la sucesión termina al llegar a uno.

# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:

nro = int(input('Escribe un número: '))

print('Secuencia de Collatz aplicada al número', nro)

while nro != 1:
    if nro % 2 == 0:
        nro = int(nro/2)
    else:
        nro = int(nro * 3 + 1)
    print(nro)
