'''
Escribir un programa que guarde en un diccionario los precios de 
las frutas de la tabla, pregunte al usuario por una fruta, un 
número de kilos y muestre por pantalla el precio de ese número 
de kilos de fruta. Si la fruta no está en el diccionario debe 
mostrar un mensaje informando de ello.
'''
frutas = {
    'platano':1.35, 
    'manzana':0.80, 
    'pera':0.85,
    'naranja':0.70}
fruta = input("Dime una fruta: ")
kilos = float(input("Cuantos kilos quieres: "))
if fruta in frutas:
    print(kilos, " kilos de ", fruta, " valen ", round(frutas[fruta]*kilos,1))
else:
    print("Lo siento, la fruta ", fruta, " no esta disponible")




