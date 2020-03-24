'''
Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad).
'''
edad = int(input("Dime tu edad: "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")