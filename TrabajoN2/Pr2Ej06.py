from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
from typing import List, Union

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    num_list = []
    str_list = []
    for elem in lista:
        if type(elem) == int or type(elem) == float:
            num_list.append(elem)
        else:
            str_list.append(elem)
    for elem in num_list:
        lista.remove(elem)
    lista.extend(num_list)
    lista.extend(str_list)
    return lista
print(numeros_al_final_basico([3, "a", 1, "b", 10, "j"]))

###############################################################################

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    num_list = []
    str_list = []
    for elem in lista:
        if isinstance(elem, float) or isinstance(elem, int):
            num_list.append(elem)
        else:
            str_list.append(elem)
    return str_list + num_list
print(numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]))