edad = int(input('Ingresa la edad: '))

if edad <= 4:
    print('Entra gratis')
elif edad >= 5 and edad <= 18:
    print('Paga 15')
else:
    print('Paga 25')