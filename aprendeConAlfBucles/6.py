'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de 
más abajo, de altura el número introducido.
'''
num = int(input("Dime numero entero: "))
for n in range(num):
    for i in range(n+1):
        print("*", end="") #end="" evita el salto de linea
    print("")#mete un salto de linea