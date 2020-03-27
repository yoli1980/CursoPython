'''
Escribir una función max_in_list() que tome una lista de 
números y devuelva el mas grande.
'''

def max_in_list(lista):
    return max(lista)
  
def max_in_lista(lista):
    num = 0
    for i in lista:
        if i > num:
            num = i
    return num

print(max_in_lista([1,2,56,89]))