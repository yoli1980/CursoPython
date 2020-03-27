'''
Definir una función superposicion() que tome dos listas y 
devuelva True si tienen al menos 1 miembro en común o devuelva 
False de lo contrario. Escribir la función usando el bucle for anidado.
'''
def superposicion(lista1, lista2):
    for i in lista1:
        for f in lista2:
            if i == f:
                return True
    return False

print(superposicion([1,2,3],[3,4,5]))