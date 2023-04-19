try:
    num1 = float(input("Ingrese el dividendo: "))
    num2 = float(input("Ingrese el divisor: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: El divisor no puede ser cero")
