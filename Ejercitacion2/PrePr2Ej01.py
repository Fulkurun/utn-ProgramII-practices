#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
numeros = input("Ingresa una lista de números separados por comas: ")
numeros = [int(x.strip()) for x in numeros.split(",")]
maximo = max(numeros)
maximo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
print("El máximo es:", maximo)
#FIN

