'''
Escribir un programa que cree un diccionario vacío y 
lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato 
debe imprimirse el contenido del diccionario.
'''
datos = {}
aniadir = "si"
while aniadir == "si":
    dato = input("Introduce tipo de dato: ")
    valor = input("Introduce el valor: ")
    datos[dato] = valor
    print(datos)
    aniadir = input("Quieres añadir algun dato mas? si/no ")


