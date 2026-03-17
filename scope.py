# Variables globales inicializadas en None
_global_int = None
_global_str = None

def set_globals(some_int, some_str):
    """
    Propósito: Almacenar un entero global y una cadena de texto global.
    Entrada:
        some_int — un valor entero.
        some_str — un valor de cadena de texto.
    Salida:
        Ninguna.
    """
    global _global_int, _global_str
    _global_int = some_int
    _global_str = some_str

def get_globals():
    """
    Propósito: Recuperar los valores de las variables globales.
    Entrada:
        Ninguna.
    Salida:
        Una tupla (int_value, str_value) que contiene el entero global y la cadena almacenados.
        Si las variables globales no han sido asignadas, sus valores por defecto son None.
    """
    return (_global_int, _global_str)
print(get_globals())       # Salida: (None, None)
set_globals(10, "Hello")
print(get_globals())       # Salida: (10, "Hello")