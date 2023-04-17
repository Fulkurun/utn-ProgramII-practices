nombre1 = "Kevin"
edad1 = 24
nombre2 = "Kevin"
edad2 = 41
resultado = (nombre1 == nombre2) and (edad1 != edad2)
print(resultado) 


marca = "Chevrolet"
modelo = 1998
resultado = (marca != "Ford") and (modelo <= 2000)
print(resultado) 

campo1 = 85121
campo2 = 851212
campo3 = 8512

resultado = campo1 < campo2 > campo3

print(resultado)


bananas = int(input("Ingrese Cantidad de Bananas: "))
naranjas = 400
manzanas = 300
peras = 30
resultado = bananas < naranjas/2 < 2*manzanas <= peras**2
print(resultado) 
