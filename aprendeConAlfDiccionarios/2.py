'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección 
y teléfono y lo guarde en un diccionario. Después debe mostrar por 
pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y 
su número de teléfono es <teléfono>..
'''
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direccion = input("Dime tu direccion: ")
tlf = input("Dime tu tlf: ")
datos = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "tlf": tlf}
print(datos["nombre"], "tiene", datos["edad"], "años, vive en", datos["direccion"], "y su numero de telefono es", datos["tlf"])
