"""DECORADORES EN PYTHON"""
"""Creación de función decoradora"""

def funcionA(funcionB):
    def funcionC(*args,**kwargs):
        print("Antes de ejecutar a la función a decorar")
        resultado=funcionB(*args,**kwargs)
        print("Despues de ejecutar a la función a decorar")
        return resultado
    return funcionC

@funcionA
def suma(a,b,c):
    s=a+b+c
    return print(s)
"""Todo lo que va luego de una función se deja dos líneas."""
"""Todo lo que va luego de una función se deja dos líneas."""
suma(30,40,70)