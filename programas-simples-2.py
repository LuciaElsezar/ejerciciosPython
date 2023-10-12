# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas.
horaActual = int(input('Escribe la Hora actual: '))
horasPasadas = int(input('Escribe la cantidad de horas que van a pasar: '))
horasDiferencia = horaActual + horasPasadas
cantidadDias = int(horasDiferencia / 24)
horaFutura = 0

if horaActual >= 0 and horaActual <=24:
    horaFutura = horasDiferencia - (24 * cantidadDias)
    print('En ', horasPasadas, 'horas, serán las: ',horaFutura)
else:
    print('Ingresar una hora válida')