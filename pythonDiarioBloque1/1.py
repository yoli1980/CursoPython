'''
Definir una función max() que tome como argumento dos 
números y devuelva el mayor de ellos. (Es cierto que 
python tiene una función max() incorporada, pero hacerla 
nosotros mismos es un muy buen ejercicio.
'''
def maximo(a,b):
    if a > b:
        print(str(a) + " es mayor que " + str(b))
    elif b > a:
        print(str(b) + " es mayor que " + str(a)) 
    else:
        print(str(a) + " y " + str(b) + " son iguales")
maximo(40,40)
