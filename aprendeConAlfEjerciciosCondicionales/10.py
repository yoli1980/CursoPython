

print("Tipos de pizza:\n1.Vegetariana\n2.No vegetariana")
pizza = input("Introduce el numero del tipo de pizza que quieres: ")
if pizza == 1:
    print("Ingredientes de pizza vegetariana:\n1.Pimiento\n2.Tofu")
    ingrediente = input("Introduce el numero del ingrediente que quieres: ")
    if ingrediente == 1:
        print("Tu pizza vegetariana lleva mozzarella, tomate y pimiento")
    else:
        print("Tu pizza vegetariana lleva mozzarella, tomate y tofu")
else:
    print("Ingredientes de pizza no vegetariana:\n1.Peperoni\n2.Jamon\n3.Salmon")
    ingrediente = input("Introduce el numero del ingrediente que quieres: ")
    if ingrediente == 1:
        print("Tu pizza no vegetariana lleva mozzarella, tomate y peperoni")
    elif ingrediente == 2:
        print("Tu pizza no vegetariana lleva mozzarella, tomate y jamon")
    else:
        print("Tu pizza no vegetariana lleva mozzarella, tomate y salmon")
