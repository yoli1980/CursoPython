'''
Escribir una función filtrar_palabras() que tome 
una lista de palabras y un entero n, y devuelva 
las palabras que tengan mas de n caracteres.
'''

def filtrar_palabras(lista,n):
    palabras = ""
    for i in lista:
        if len(i) > len(palabras):
            palabras = i
    return palabras

print(filtrar_palabras(["hola","adios","hasta pronto"], 5))