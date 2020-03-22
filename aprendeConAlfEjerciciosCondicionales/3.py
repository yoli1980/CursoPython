'''
Escribir un programa que pida al usuario 
dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar 
un error.
'''
dividendo = float(input("Dame un dividendo: "))
divisor = float(input("Dame un divisor: "))
if divisor == 0:
    print("Dame un divisor que no sea 0")
else:
    print("Resultado: " + str(dividendo / divisor))