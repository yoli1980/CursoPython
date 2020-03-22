'''
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras 
vendidas que no son del día. Después el programa debe mostrar 
el precio habitual de una barra de pan, el descuento que se le 
hace por no ser fresca y el coste final total.
'''

barras = int(input("Dime el numero de barras vendidas que no son del dia: "))
precio = 3.49
descuento = 0.60
coste = barras * precio * (1 - descuento)
print("El precio de una barra de pan es de " + str(precio) + " euros")
print("Tiene un descuendo del " + str(descuento*100) +  " % por no ser fresca")
print("Coste final total: " + str(round(coste)) + " euros")
