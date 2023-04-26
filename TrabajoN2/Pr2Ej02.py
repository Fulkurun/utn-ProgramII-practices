def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.

    Restricciones:
        - Utilizar comparaciones encadenadas.
        - Utilizar UNICAMENTE dos IFs
        - No utilizar ELSE
        - No utilizar AND, OR o NOT

    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons # noqa: E501
    """
def maximo_encadenado(a: float, b: float, c: float) -> float:
    if a > b > c:
        return a
    if b > a > c:
        return b
    return b
print(maximo_encadenado(1, 10, 5))
print(maximo_encadenado(5, 10, 1))
print(maximo_encadenado(5, 10, 5))
def maximo_encadenado(a: float, b: float, c: float) -> float:
    if c > b > a:
        return c
    if a > b > c:
        return b
    return c
print(maximo_encadenado(4, 9, 18))
print(maximo_encadenado(9, 4, 18))
print(maximo_encadenado(9, 9, 18))
def maximo_encadenado(a: float, b: float, c: float) -> float:
    if a > c > b:
        return a
    if b < c > a:
        return b
    return a
print(maximo_encadenado(24, 9, 18))
print(maximo_encadenado(24, 18, 9))
print(maximo_encadenado(24, 18, 18))

###############################################################################

def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    """Re-escribir para que tome 4 parámetros, utilizar la función max.

    Referencia: https://docs.python.org/3/library/functions.html#max"""
def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    return max(a, b, c, d)
print(maximo_cuadruple(1, 10, 5, -5))
print(maximo_cuadruple(4, 9, 18, 6))
print(maximo_cuadruple(24, 9, 18, 20))
print(maximo_cuadruple(24, 9, 18, 30))

###############################################################################

def maximo_arbitrario(*args) -> float:
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists # noqa: E501
    """
def maximo_arbitrario(*args) -> float:
    return max(*args)
print(maximo_arbitrario(1, 10, 5, -5))
print(maximo_arbitrario(4, 9, 18, 6))
print(maximo_arbitrario(24, 9, 18, 20))
print(maximo_arbitrario(24, 9, 18, 30))