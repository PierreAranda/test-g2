

import time

"""DECORADORES EN PYTHON"""

"""Creación de función decoradora"""
"""Tiempo de ejecución de un función"""


def mesuretime(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print("La demora en ejecutar fue de: {}".format(total))
        return result
    return wrapper


"""Permite decorar"""


@mesuretime
def suma(a, b, c, d):
    time.sleep(1)
    """Permite un retraso en la ejecución del código"""
    s = a+b+c+d
    return s


print(suma(20, 40, 60, 100))
