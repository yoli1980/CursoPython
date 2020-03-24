'''
Escribir un programa que pida al usuario un número 
entero y muestre por pantalla si es un número 
primo o no.
'''
num = int(input("Dime un numero positivo mayor que 2: "))
n = 2
while num % n != 0:
    n += 1
if n == num:
    print(str(num) + " es primo")
else:
    print(str(num) + " no es primo")

