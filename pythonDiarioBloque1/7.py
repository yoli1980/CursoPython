'''
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True
'''
palabra = input("Introduce una palabra: ")
alreves = palabra
palabra = list(palabra)
alreves = list(alreves)
alreves.reverse()
if palabra == alreves:
    print("Es un palindromo")
else:
    print("No es palindromo")
