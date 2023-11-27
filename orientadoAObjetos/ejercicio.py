class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def setTitular(self):
        self.titular = input("Escribe el nombre del titular: ")
    
    def setCantidad(self):
        self.cantidad = input("Escribe la cantidad de dinero: ")
    
    def getTitular(self):
        return self.titular
    
    def getCantidad(self):
        return print("Cantidad: ",self.cantidad)
    
    def mostrar(self):
        return print("Hola titular ", self.titular, ",\ntienes ", self.cantidad, ", en algo!!!!!!")
    
    def ingresar(self, cantidad):
        if cantidad >= 1:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        if self.cantidad <= -1:
            print("Numeros negativos. Te vas a ir a la carcel >:(.")

juan = Cuenta("Juan")

juan.getCantidad()
