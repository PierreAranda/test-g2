

"""DECORADORES EN PYTHON"""
"""Creación de función decoradora"""


def funcionA(funcionB):
    """Función interna de la función decoradora"""
    def funcionC(*args,**kwargs):   #'*argas': Indica una cantidad "x" de parametros
                                    #'**kwars': Indica una cantidad "x" de parametros
        print("Antes de ejecutar la función a decorar")
        resultado=funcionB(*args,**kwargs)
        print("Despues de ejecutar la función a decorar")
        return resultado

    return funcionC

"""Función a decorar""" #Amarillo aparece por falta de 'PEP 8'
@funcionA
def saludar(nombre):
    return "Hola {}".format(nombre)

saludo=input("Ingrese su nombre: \n")
print(saludar(saludo))
