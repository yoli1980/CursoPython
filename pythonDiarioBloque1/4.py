'''
Escribir una función que tome un carácter y devuelva True 
si es una vocal, de lo contrario devuelve False.
'''
def es_vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    else:
        return False
    
print(es_vocal("t"))
print(es_vocal("o"))