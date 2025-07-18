idade = int(input("Digite sua idade: "))

if idade < 0:
    print("A idade não pode ser negativa!")
elif idade <= 12:
    print("É uma criança.")
elif idade <= 17:
    print("É um adolescente.")
elif idade <= 64:
    print("É um adulto.")
else:
    print("É um idoso.")
