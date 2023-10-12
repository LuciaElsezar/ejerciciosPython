estatura = float(input('Escribir la estatura: '))
peso = int(input('Escribir el peso: '))
edad = int(input('Escribir la edad: '))
if estatura >= 3.5:
    indiceMasaCorporal = int(peso / (estatura / 100))
else:
    indiceMasaCorporal = int(peso / estatura)

print('IMC: ', indiceMasaCorporal)

if edad >= 45:
    if indiceMasaCorporal >= 22:
        print('Riesgo alto.')
    else:
        print('Riesgo medio.')
else:
    if indiceMasaCorporal >= 22:
        print('Riesgo medio.')
    else:
        print('Riesgo bajo.')

# La masa corporal de 22 es poca para lo considerado normal