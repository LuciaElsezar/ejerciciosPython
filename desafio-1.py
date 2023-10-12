# Este problema apareció en el certamen recuperativo 1 
# del segundo semestre de 2011 en el campus Vitacura.

# Una máquina de alimentos tiene productos de tres tipos, A, B y C, 
# que valen respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10, $50 y $100.

# Escriba un programa que pida al usuario elegir el producto y 
# luego le pida ingresar las monedas hasta alcanzar el monto a pagar. 
# Si el monto ingresado es mayor que el precio del producto, 
# el programa debe entregar las monedas de vuelto, una por una.

producto = ['A', 'B', 'C']
precio = [270, 340, 390]
monedas = [10, 50, 100]
monedasADevolver = []

dineroRecibido = 0
monedaDada = 0
cambio = 0

productoPreguntado = False
productoPagado = False
productoIndex = 0

monedasDe10 = 0
monedasDe50 = 0
monedasDe100 = 0

while productoPreguntado == False:
        productoIndex = int(input('''Elige un tipo de producto: 
                                    -- 1 para un producto tipo A 
                                    -- 2 para un producto tipo B 
                                    -- 3 para un producto tipo C \n
                                    -----> ''')) - 1
        if productoIndex < 0 or productoIndex > 2:
            print('\n Producto no válido. Inentando nuevamente...\n')
        else:
            productoPreguntado = True

print('Ha elegido el producto', producto[productoIndex], 'y cuesta $', precio[productoIndex])

while productoPagado == False:
        print('Faltan $', precio[productoIndex] - dineroRecibido, 'para pagar por el producto.')
        monedaDada = int(input('''Elige una moneda a ingresar: 
                                    -- 10 para una moneda de 10
                                    -- 50 para una moneda de 50 
                                    -- 100 para una moneda de 100
                                    -- Otro cambio no será válido \n
                                    -----> '''))
        if monedaDada not in monedas:
            print('Moneda no válida. Inentando nuevamente...\n')
        else: 
            dineroRecibido += monedaDada
            if dineroRecibido >= precio[productoIndex]:
                 break

cambio = int(dineroRecibido - precio[productoIndex])

print('Ingresaste un total de $', dineroRecibido, 'Devolviendo $', cambio, '...')

while cambio != 0:
    for i in range(len(monedas) -1 , -1 , -1):
        if cambio >= monedas[i]:
            cambio -= monedas[i]
            if monedas[i] == 10:
                monedasDe10 += 1
            if monedas[i] == 50:
                monedasDe50 += 1
            if monedas[i] == 100:
                monedasDe100 += 1            

print('El cambio que va a recibir es:')
if monedasDe10 >= 1:
    print('--',monedasDe10,'monedas de $ 10')
if monedasDe50 >= 1:
    print('--',monedasDe50,'monedas de $ 50')    
if monedasDe100 >= 1:
    print('--',monedasDe100,'monedas de $ 100')
          
     