'''
Escribir un programa que le diga al usuario 
que ingrese una cadena. El programa tiene que 
evaluar la cadena y decir cuantas letras mayúsculas tiene.
'''


def mayusculas():
    cadena = input("Introduce una cadena de caracteres: ")    
    mayusculas = 0
    for i in cadena:
        if i != i.lower():
            mayusculas += 1
    print(mayusculas)
        
mayusculas()