'''
Los alumnos de un curso se han dividido en dos 
grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un 
nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario 
su nombre y sexo, y muestre por pantalla el grupo 
que le corresponde.
'''
nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo (H o M): ")
if (sexo == "M" and nombre.lower() < "m") or (sexo == "H" and nombre.lower() > "n"):
    grupo = "A"
else:
    grupo = "B"
print("Perteneces al grupo " + grupo)
