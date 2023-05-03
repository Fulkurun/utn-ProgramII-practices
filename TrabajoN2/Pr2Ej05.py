def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """

def sumatoria_basico(n: int) -> int:
    resultado = 0
    for i in range(1, n+1):
        resultado += i
    return resultado

print(sumatoria_basico(1))
print(sumatoria_basico(100))

###############################################################################

def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
def sumatoria_sum(n: int) -> int:
    return sum(range(1, n+1))
print(sumatoria_sum(1))
print(sumatoria_sum(100))

###############################################################################

from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
from typing import Iterable
def multiplicar_basico(numeros: Iterable[float]) -> float:
    result = 1.0
    for num in numeros:
        result *= num
        if num == 0:
            return 0.0
    return result

print(multiplicar_basico([1, 2, 3, 4]))
print(multiplicar_basico([2, 5]))
print(multiplicar_basico([0]))
print(multiplicar_basico([1, 2, 3, 0, 4, 5]))

