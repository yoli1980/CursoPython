'''
Escribir un programa que pregunte al usuario por el número 
de horas trabajadas y el coste por hora. Después debe 
mostrar por pantalla la paga que le corresponde.
'''
num_horas = float(input("Dime el numero de horas trabajadas: "))
coste_hora = float(input("Dime el coste de la hora: "))
print("Te corresponde cobrar " + str(num_horas*coste_hora) + " euros")