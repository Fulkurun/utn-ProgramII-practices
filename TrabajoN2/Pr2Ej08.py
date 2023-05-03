from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción:
        - Utilizar un bucle FOR.
        - Utilizar la función range.
        - Utilizar índices.
    """
def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    return tuple(zip(nombres, precios))
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)
print(combinar_basico(nombre_articulos, precio_articulos) == respuesta)

###############################################################################

id_articulos = [6852, 1459, 3578]
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]

def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    """Re-Escribir utilizando enumerate y agregando un nuevo componente.

    Restricción:
        - Utilizar un bucle FOR.
        - No Utilizar la función range.
        - No Utilizar la función zip.

    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """

def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    resultado = []
    for i, nombre in enumerate(nombres):
        resultado.append((nombre, precios[i], ids[i]))
    return tuple(resultado)
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)
print(combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta)

###############################################################################

id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    """Re-Escribir utilizando zip.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """
def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    return tuple(zip(nombres, precios, ids))
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)
print(combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta)

###############################################################################

id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:
    """Re-Escribir utilizando zip y una cantidad arbitraria de componentes.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices."""
    
from typing import Any, List, Tuple
def combinar_zip_args(*args) -> Tuple[Any]:
    listas = list(args)
    combinado = zip(*listas)
    resultado = tuple(tuple(elem) for elem in combinado)
    return resultado


respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]
print(combinar_zip_args(*componentes) == respuesta)
