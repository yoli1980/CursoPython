'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que 
el usuario tiene que repetir.
'''
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input("Que nota has sacado en " + asignatura + "?"))
    if nota >= 5:
        notas.append(asignatura)
for asignatura in notas:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))
