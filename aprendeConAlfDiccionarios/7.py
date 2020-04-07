'''
Escribir un programa que cree un diccionario simulando 
una cesta de la compra. El programa debe preguntar el artículo 
y su precio y añadir el par al diccionario, hasta que el 
usuario decida terminar. Después se debe mostrar por pantalla 
la lista de la compra y el coste total, con el siguiente formato
'''
cesta = {}
mas = "si"
while mas == "si":
    articulo = input("Introduce articulo: ")
    precio = float(input("Introduce precio: "))
    cesta[articulo] = precio
    mas = input("Quieres añadir algun articulo mas?(si/no) ")
coste = 0
print("Lista de la compra")
for articulo, precio in cesta.items():
    print(articulo, "\t", precio)
    coste += precio
print("Coste total: " + str(coste))




