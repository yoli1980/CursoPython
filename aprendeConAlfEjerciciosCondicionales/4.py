'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par 
o impar.
'''
num = int(input("Dame un numero entero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")