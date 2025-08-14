inventario = {
    "chocolate": 10,
    "chiclete": 5,
    "paleta": 8,
    "mashmellow": 5,
    "jujuba": 2,
    "pirulito": 12,
}

carrinho = []

for doce, preco in inventario.items():
    print(f"{doce.capitalize()} - R${preco}")

while True:
    opcoes = input("Qual doce deseja comprar? (Escreva 'Sair' para terminar)").lower()

    if opcoes == "Sair":
        break
    if opcoes in inventario:
        carrinho.append(opcoes)
        print(f"Adicionou {opcoes.capitalize()} no carrinho.")
    else:
        print("Esse produto não esta no carrinho, tente novamente.")

total = 0
print("Seu carrinho:")
for doce in carrinho:
    print(f"{doce.captalize()} - R${inventario[doce]}")
    total += inventario[doce]

print(f"Total a pagar: R${total}")
print("Obrigada pela compra, volte sempre!")
