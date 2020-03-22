'''
Escribir un programa que pregunte el nombre del usuario en la 
consola y un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre = input("Dime tu nombre: ")
num = int(input("Dime un numero entero: "))
print((nombre + "\n") * num)