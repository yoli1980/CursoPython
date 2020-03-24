'''
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión cada año 
que dura la inversión.
'''
cantidad = float(input("Dime la cantidad a invertir: "))
interes = float(input("Dime el interes anual: "))
anios = int(input("Dime el numero de años: "))
for a in range(anios):
    cantidad *= 1 + interes / 100
    print("Capital tras " + str(a+1) + " años: " + str(round(cantidad, 2)))