'''
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.
'''

password = "habitacion"
contrasenia = ""
while contrasenia != password:
    contrasenia = input("Introduce la contraseña: ")
print("Contraseña correcta")