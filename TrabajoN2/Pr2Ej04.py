def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns."""

def es_vocal_if(letra: str) -> bool:
    letra = letra.lower()
    if letra == 'a':
        return True
    if letra == 'e':
        return True
    if letra == 'i':
        return True
    if letra == 'o':
        return True
    if letra == 'u':
        return True
    return False
print(es_vocal_if("a"))
print(not es_vocal_if("b"))
print(es_vocal_if("A"))
print(es_vocal_if("e"))
print(es_vocal_if("E"))

###############################################################################

def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas."""
    
def es_vocal_if_in(letra: str) -> bool:
    letra = letra.lower()
    
    if letra in "aeiou":
        return True
    
    return False
print(es_vocal_if_in("a"))
print(not es_vocal_if_in("b"))
print(es_vocal_if_in("A"))

###############################################################################

def es_vocal_in(letra: str) -> bool:
    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """

def es_vocal_in(letra: str) -> bool:
    return letra.lower() in "aeiou"
print(es_vocal_in("a"))
print(not es_vocal_in("b"))
print(es_vocal_in("A"))
