list_invitados = {
    "juan" : "45544646l",
    "maria" : "25764t",
    "laura" : "54315468y",
    "pepe" : "21548465l",
    "bea" : "26668465l"
}

num_invitados = len(list_invitados)
#al igual que hacemos con int para transfomar a entero, en este caso 
#para tener #los valores en forma de lista ponemos list. 

invitados = list(list_invitados.values())

while num_invitados >= 1:
    dni = input("Dime tu dni: ")
    for i in invitados:
        if i == dni:
            print("puedes pasar")
            num_invitados -=1
            invitados.remove(i)
            print("Quedan por entrar "+ str(num_invitados))
            break
    if i != dni:
        print("Seguridad!!!") 
 
print("Ya están todos los invitados")