'''
Escribir un programa que muestre el eco de todo lo que el 
usuario introduzca hasta que el usuario escriba “salir” 
que terminará.
'''
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        print("Fin del juego")
        break           
    print(frase)
    