'''Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
una divisa y muestre su símbolo o un mensaje de aviso si la divisa 
no está en el diccionario.
'''
monedas = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'}

moneda = input("Dime una divisa: ")
print(monedas.get(moneda.title(), "No se encuentra esa divisa"))





