'''
Definir una función que calcule la longitud de una lista o 
una cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un 
muy buen ejercicio.
'''


def longitud(lista):
    contador = 0
    for i in lista:
        contador += 1
    return contador

print(longitud([1,2,3,4,5]))