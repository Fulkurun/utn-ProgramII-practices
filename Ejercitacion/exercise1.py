"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = lado_cuadrado*lado_cuadrado
print(f"area del cuadrado es",area_cuadrado)
# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = lado_cuadrado**2
print(f"usando potencia",area_cuadrado)
# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = pow(lado_cuadrado, 2)
print(f"usando funcion pow",area_cuadrado)
# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
cantidad_a_comprar = presupuesto_disponible // precio
print("Puedes comprar", cantidad_a_comprar, "unidades.")
# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO

numero_incalculable = 2 ** 54 - 1
es_divisible_por_siete= numero_incalculable
if numero_incalculable % 7 == 0:
    print(numero_incalculable, "es divisible por 7")
else:
    print(numero_incalculable, "no es divisible por 7")


# COMPLETAR - FIN

assert es_divisible_por_siete