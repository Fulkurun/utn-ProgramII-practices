from typing import Union
def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - Utilizar IF con ELIF con ELSE.
        - No utilizar AND ni OR.
    """
from typing import Union
def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    if multiplicar:
        return a * b
    elif not multiplicar and b == 0:
        return "Operación no válida"
    else:
        return a / b
print(operacion_basica(1, 1, True))
print(operacion_basica(1, 1, False))
print(operacion_basica(25, 5, True))
print(operacion_basica(25, 5, False))
print(operacion_basica(0, 5, True))
print(operacion_basica(0, 5, False))
print(operacion_basica(1, 0, True))
print(operacion_basica(1, 0, False))

###############################################################################

from typing import Union
def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501
    """Re-Escribir el ejercicio anterior utilizando tres returns.

    Restricciones:
        - Utilizar 2 IF.
        - No Utilizar IF anidados.
        - No utilizar ELIF ni ELSE.
        - No utilizar AND ni OR.
    """
from typing import Union
def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    if multiplicar:
        return a * b
    if not b:
        return "Operación no válida"
    return a / b
print(operacion_multiple(1, 1, True))
print(operacion_multiple(1, 1, False))
print(operacion_multiple(25, 5, True))
print(operacion_multiple(25, 5, False))
print(operacion_multiple(0, 5, True))
print(operacion_multiple(0, 5, False))
print(operacion_multiple(1, 0, True))
print(operacion_multiple(1, 0, False))
