class Vehiculo:
    
    def __init__(self, marca, ruedas, color, enMarcha=False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha
    
    def arrancar(self):
        self.enMarcha = True
    
    def tipoVehiculo(self):
        if self.ruedas == 4:
            return "Automovil"
        elif self.ruedas == 2:
            return "Motocicleta"
        else:
            return "Desconocido"
    
    def mostrar(self):
        print("Marca:", self.marca)
        print("Ruedas:", self.ruedas)
        print("Color:", self.color)
        print("En marcha:", self.enMarcha)

mi_coche = Vehiculo("nissan", 3, "celeste")
print(mi_coche.tipoVehiculo())
mi_coche.arrancar()
mi_coche.mostrar()