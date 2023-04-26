def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor.

    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """
    if a > b:
        return a
    if b > a:
        return b
    return a
print(maximo_basico(10 , 5))
print(maximo_basico(9, 18))

###############################################################################

def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """
def maximo_libreria(a: float, b: float) -> float:
    return max(a, b)
print(maximo_libreria(10, 5))
print(maximo_libreria(9, 18))

###############################################################################

def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """
def maximo_ternario(a: float, b: float) -> float:
    return a if a > b else b
print(maximo_ternario(10, 5))
print(maximo_ternario(9, 18))