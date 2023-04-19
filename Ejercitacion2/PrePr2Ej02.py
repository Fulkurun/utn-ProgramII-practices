#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenes en otra lista de numeros impares.

#El programa debe mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
numeros = input("Ingrese una lista de numeros separados por coma: ")
lista_numeros = numeros.split(",")
lista_impares = []

for num in lista_numeros:
    if int(num) % 2 != 0:
        lista_impares.append(int(num))

print("Lista de numeros originales:", lista_numeros)
print("Lista de numeros impares:", lista_impares)
#ALETA