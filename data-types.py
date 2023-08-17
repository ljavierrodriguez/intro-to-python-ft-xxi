""" Data Types """
"""  

String
Boolean
Int
Float

None

dict

Array:
    List
    Tuples
    Set

func

"""

nombre = "John"
apellido = 'Doe'
nombre_completo ='''John Doe'''

active = False
open = True

edad = 40 
temp = -10.5

direccion = None

persona = {
    "nombre": "",
    "apellido": ""
}

# list
notas = [1, 2, 3, 4]
notas[0]

# tuples
status = ("active", "inactive", "suspended", "canceled", "success", "fail")
status[0]

# sets
frutas = { "Manzana", "Pera", "Uva" }
grados = { 1, 2, 3 }


def sumar(a, b):
    return a + b

sumar = lambda a, b: a + b
    
def restar():
    pass

def multiplicar(a: int, b: int) -> int:
    return a * b
