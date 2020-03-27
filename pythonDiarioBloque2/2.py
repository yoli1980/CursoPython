'''
Escribir una función mas_larga() que tome una lista 
de palabras y devuelva la mas larga.
'''

def mas_larga(lista):
    maslarga = ""
    for i in lista:
        if len(i) > len(maslarga):
            maslarga = i
    return maslarga

print(mas_larga(["hola","adios","hasta luego","hasta pronto"]))