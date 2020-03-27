'''
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena 
"odnaborp yotse"
'''
def inversa(cadena):
    cadena = list(cadena)
    cadena.reverse()
    cad = "".join(cadena)
    print(cad)

inversa("hola")