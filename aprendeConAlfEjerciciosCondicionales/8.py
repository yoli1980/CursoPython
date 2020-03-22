'''
Escribir un programa que lea la puntuación del usuario 
e indique su nivel de rendimiento, así como la cantidad 
de dinero que recibirá el usuario.
'''
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuacion: "))

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""

if nivel == "":
    print("Esta puntuacion no es valida")
else:
    print("Tu nivel de rendimiento es " + nivel)
    print("Recibiras " + str(puntos * bonificacion))