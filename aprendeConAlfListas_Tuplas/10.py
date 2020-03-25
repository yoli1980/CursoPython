'''
Escribir un programa que almacene en una lista los siguientes 
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y 
el mayor de los precios.
'''
precios = [50, 75, 46, 22, 80, 65, 8]
for precio in precios:
    menor = min(precios)
    mayor = max(precios)
print("El mínimo es " + str(menor)) 
print("El máximo es " + str(mayor))
    