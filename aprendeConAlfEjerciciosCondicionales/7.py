'''
Escribir un programa que pregunte al usuario su renta anual 
y muestre por pantalla el tipo impositivo que le corresponde.
'''
renta = float(input("Dime tu renta anual: "))
if renta < 10000:
    tipo = 5    
elif renta >= 10000 and renta <= 20000:
    tipo = 15
elif renta >= 20000 and renta <= 35000:
    tipo = 20
elif renta >= 35000 and renta <= 60000:
    tipo = 30
else:
    tipo = 45
print("Te corresponde el tipo impositvo del " + str(tipo) + "%")