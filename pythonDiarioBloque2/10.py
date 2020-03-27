'''
Escriba una función es_bisiesto() que determine 
si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100. 
También es divisible por 400
'''

def es_bisiesto():
    anio = int(input("Introduzca el año a comprobar: "))
    if anio % 4 == 0 and (not(anio % 100 == 0)):
        print(str(anio) + " es bisiesto")
    elif anio % 400 == 0:
        print(str(anio) + " es bisiesto")
    else:
        print(str(anio) + " no es bisiesto")
        
es_bisiesto()     