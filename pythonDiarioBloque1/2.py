'''
Definir una función max_de_tres(), que tome tres números 
como argumentos y devuelva el mayor de ellos.
'''
def maxim(a,b,c):
    if a > b and a > c:
        print(str(a) + " es mayor que " + str(b) + " y " + str(c))
    elif b > a and b > c:
        print(str(b) + " es mayor que " + str(a)  + " y " + str(c)) 
    elif c > a and c > b:
        print(str(c) + " es mayor que " + str(a)  + " y " + str(b))
    else:
        print(str(a) + " ," + str(b) + " y " + str(c) + " son iguales")
maxim(6,6,6)
