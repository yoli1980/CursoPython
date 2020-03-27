'''
Definir una lista con un conjunto de nombres, imprimir la 
cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  
'''

def buscar():
    num = int(input("¿Cuantos nombres quieres introducir?: "))
    lista = []
    for i in range(num):
        nombres = input("Introduce un nombre: ")
        lista.append(nombres)
    
    letra = input("¿Con que letra quiere que comience el nombre?: ")
    contador = 0
    for x in lista:        
        if x[0] == letra.lower() or x[0] == letra.upper():
            contador += 1
    print(contador) 
                          
buscar()