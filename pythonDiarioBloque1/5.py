'''
Escribir una funcion sum() y una función multip() que sumen y 
multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) 
debería devolver 24.
'''
def suma(lista):
    suma = 0
    for i in lista:
        suma +=i
    print(str(suma))

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *=i
    print(str(multiplicacion)) 
    
suma([1,2,3,4])
multip([1,2,3,4])