"Sabado 18/06/2022 - Hasta las 10:00pm"
"""DECORADORES EN PYTHON"""
"""Creación de función decoradora"""

def funcionA(funcionB):
    #Función interna de la función decoradora
    def funcionC():
        print("Antes de ejecutar la función a decorar")
        funcionB()
        print("Despues de ejecutar la función a decorar")

    return funcionC()

"""Función a decorar""" #Amarillo aparece por falta de 'PEP 8'
@funcionA #Permite llevar a dicha función
def saludar():
    print("Hola Susana")
