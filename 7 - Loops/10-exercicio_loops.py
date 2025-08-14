print(
    """ 
      1 - Adicionar produto
      2 - Remover produto
      3 - Lista de produtos
      4 - Buscar produto
      5 - Contar produtos
      6 - Esvaziar carrinho
"""
)

carrinho = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Açúcar",
    "Sal",
    "Óleo de soja",
    "Café",
    "Leite",
    "Farinha de trigo",
    "Sabonete",
]
opcoes = int(input("Escolha uma opção de 1 a 6: "))

if opcoes == 1:
    produto = input("Adicionar produto: ")
    if produto not in carrinho:
        carrinho.append(produto)
        print("Produto adicionado com sucesso!")
    else:
        print("Produto já existente. Adicione outro.")
elif opcoes == 2:
    remover = input("Qual item você deseja remover? ")
    if remover in carrinho:
        carrinho.remove(remover)
        print("Produto removido.")
    else:
        print("Produto não existente.")
elif opcoes == 3:
    if len(carrinho) > 0:
        print("Lista de compras: ")
        carrinho.sort()
        print(carrinho)
    else:
        print("A lista está vazia.")
elif opcoes == 4:
    busca_prod = input("Digite o produto que está buscando: ")
    if busca_prod in carrinho:
        print(f"{busca_prod} está na lista.")
    else:
        print("Este produto não está na lista")
elif opcoes == 5:
    print(f"Total de produtos no carrinho: {len(carrinho)}")
elif opcoes == 6:
    carrinho.clear()
    print("Carrinho esvaziado com sucesso.")
else:
    print("Opção inválida.")

print(carrinho)
