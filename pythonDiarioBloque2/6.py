'''
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento 
de tres personas.
- Se calcula cuántos años cumplirán durante el 
año en curso.
- Se imprime en pantalla.
'''

def cumple():
    actual = int(input("Introduce el año actual: "))
    for i in range(3):
        nombre = input("Introduce un nombre: ")
        anio = int(input("Introduce el año de nacimiento: "))        
        print(nombre + " cumple " + str(actual - anio) + " años en el " + str(actual))
        
cumple()