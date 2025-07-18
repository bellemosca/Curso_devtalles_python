shopping_cart = [
    "Camisas",
    "Tenis",
    "Calças",
    "Bermudas",
    "Cueca",
    "Chinelos",
    "Bonés",
    "Gravata",
    "Meia",
]

# new_list = shopping_cart[1:4]

# new_list[0] = "Sapatos"
# new_list[1] =  "Colar"

# print(shopping_cart[1])

# [Inicio : fim]
# print(new_list)

new_cart = shopping_cart[:]
new_cart[0] = "Sapatos"
shopping_cart[1] = "Colar"

print(shopping_cart)
print(new_cart)
