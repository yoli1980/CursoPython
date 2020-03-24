'''
Escribir un programa en el que se pregunte al usuario por una 
frase y una letra, y muestre por pantalla el número de veces 
que aparece la letra en la frase.
'''
frase = input("Dime una frase: ")
letra = input("Dime una letra: ")
contador = 0
for l in frase:
    if l == letra:
        contador += 1
print("La letra " + letra + " aparece en la frase '" + frase + "' " + str(contador) + " veces")