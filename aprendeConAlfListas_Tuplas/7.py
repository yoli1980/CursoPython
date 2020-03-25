'''
Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.
'''
abededario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(abededario)
for letra in range(len(abededario),1,-1):
    if letra % 3 == 0:
        abededario.pop(letra-1)
print(abededario)
    