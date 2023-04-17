#""""ejercicio 1"""

esta_lloviendo = True
riego_activo = True
Piso_Mojado = esta_lloviendo or riego_activo
print(Piso_Mojado)

#"""" ejercicio 2"""

area=int(input("Ingrese Area: "))
resultado = not(area <= 5)
print(resultado)
#"""" ejercicio 3"""
numero1 = 49
numero2 = 50
resultado = (numero1 % 7 == 0) and (numero2 % 7 != 0)
print(resultado) 
#"""" ejercicio 4"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100


(variable_01 and variable_03) or (not variable_01 and variable_02 and variable_03) or (variable_04 == str(variable_03) and variable_05 > variable_03)

print(resultado)



