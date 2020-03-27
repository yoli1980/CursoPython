'''
Definir una tupla con 10 edades de personas. 
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien 
ingrese las edades.
'''


def superior_a_20(tupla):
    contador = 0
    for i in tupla:
        if i > 20:
            contador += 1
    print(contador)

superior_a_20((11,20,37,49,56,65,74,8,49,10))
        