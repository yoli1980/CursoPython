'''
Escribir un programa que pida al usuario una palabra y 
muestre por pantalla si es un palíndromo.
'''
palabra = input("Dime una palabra: ")
alreves = palabra
palabra = list(palabra)
alreves = list(alreves)
alreves.reverse()
if palabra == alreves:
    print("Es un palindromo")
else:
    print("No es palindromo")