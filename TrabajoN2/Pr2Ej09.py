from typing import Iterable


def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    """Toma una lista de números, los eleva al cubo, y devuelve la suma de
    los elementos pares.

    Restricciones:
        - Utilizar dos bucles FOR.
        - No utilizar la función range."""

def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    suma = 0
    for num in numeros:
        cubo = num ** 3
        if cubo % 2 == 0:
            suma += cubo
    return suma
print(suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288)

###############################################################################

def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    """Re-Escribir utilizando comprension de listas (debe resolverse en 1
    línea) y la función built-in sum."""

def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    return sum(x ** 3 for x in numeros if x % 2 == 0)
print(suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288)

###############################################################################

numeros = [1, 2, 3, 4, 5, 6]


"""
Escribir una función lambda que eleve los elementos al cubo

Restricción: Utilizar List, map y lambda y la variable numeros
"""

numeros_al_cubo = [1, 2, 3, 4, 5, 6] 

"""
Escribir una función lambda que permita filtrar todos los elementos pares

Restricción: Utilizar List, filter, lambda y la variable numeros_al_cubo
"""

numeros_al_cubo_pares = [1, 2, 3, 4, 5, 6] 


"""
Escribir una función Lambda que sume todos los elementos

Restricción: Utilizar reduce, lambda y la variable numeros_al_cubo_pares
"""

from functools import reduce 

suma_numeros_al_cubo_pares = [1, 2, 3, 4, 5, 6]

elevar_al_cubo = lambda x: x**3
numeros_al_cubo = list(map(elevar_al_cubo, numeros))

filtrar_pares = lambda x: x % 2 == 0
numeros_al_cubo_pares = list(filter(filtrar_pares, numeros_al_cubo))

sumar_elementos = lambda x, y: x + y
suma_numeros_al_cubo_pares = reduce(sumar_elementos, numeros_al_cubo_pares)

print(numeros_al_cubo == [1, 8, 27, 64, 125, 216])
print(numeros_al_cubo_pares == [8, 64, 216])
print(suma_numeros_al_cubo_pares == 288)



