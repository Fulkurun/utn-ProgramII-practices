from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:  # noqa: E501
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricciones:
        - Utilizar dos bucles FOR anidados.
        - Utilizar dos returns.
    """
from typing import Any, Iterable
def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    set_1 = set(lista_1)
    set_2 = set(lista_2)
    return bool(set_1 & set_2)
test_list = [1, "hello", 35.20]
print(superposicion_basico(test_list, (2, "world", 35.20)))
print(not superposicion_basico(test_list, (2, "world", 30.85)))

###############################################################################

def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN.

    Restricciones:
        - Utilizar un único bucle FOR.
        - Utilizar dos returns.
    """
def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for elem_1 in lista_1:
        if elem_1 in lista_2:
            return True
    return False
test_list = [1, "hello", 35.20]
print(superposicion_in(test_list, (2, "world", 35.20)))
print(not superposicion_in(test_list, (2, "world", 30.85)))

###############################################################################

def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando la funcion any.

    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea."""
def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return any(elemento in lista_2 for elemento in lista_1)
test_list = [1, "hello", 35.20]
print(superposicion_any(test_list, (2, "world", 35.20)))
print(not superposicion_any(test_list, (2, "world", 30.85)))

###############################################################################

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).

    Restricciones:
        - Resolver sólo utilizando operaciones de conjuntos
        - No utilizar ANY, ALL, FOR, IF ni COMPRENSIONES."""

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    set_1 = set(lista_1)
    set_2 = set(lista_2)
    return len(set_1.intersection(set_2)) > 0
test_list = [1, "hello", 35.20]
print(superposicion_set(test_list, (2, "world", 35.20)))
print(not superposicion_set(test_list, (2, "world", 30.85)))
