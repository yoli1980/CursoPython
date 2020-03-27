'''
Crear una función contar_vocales(), que reciba una 
palabra y cuente cuantas letras "a" tiene, cuantas letras 
"e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
'''

def contar_vocales():
    cadena = input("Introduce una cadena: ")
    cadena = cadena.lower()
    vocales = "aeiou"
   
    for x in vocales:
        contador = 0
        for z in cadena:
            if z == x:
                contador += 1
        #print("Hay %d %s." % (contador, x))
        print("Hay {0} {1}.".format(contador, x))

contar_vocales() 
        