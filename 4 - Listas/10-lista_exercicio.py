# Criar um carrinho de compras que faça as seguintes operações:
# - Adicionar um item ao carrinho
# - Remover um item do carrinho
# - Listar os itens do carrinho
# - Buscar produtos
# - Contar produtos do carrinho
# - Esvaziar o carrinho

# -----------------------------------------------------------------------------
# # Caminho do arquivo que vai armazenar o carrinho
# CAMINHO_ARQUIVO = "carrinho.txt"

# # Função para carregar os produtos salvos
# def carregar_carrinho():
#     # Verifica se o arquivo existe
#     if os.path.exists(CAMINHO_ARQUIVO):
#         # Abre o arquivo em modo leitura e lê todas as linhas, removendo quebras de linha
#         with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
#             return [linha.strip() for linha in arquivo.readlines()]
#     # Se o arquivo não existir, retorna uma lista vazia
#     return []

# # Função para salvar os produtos no arquivo
# def salvar_carrinho(carrinho):
#     # Abre o arquivo em modo escrita (apaga conteúdo anterior) e escreve cada produto
#     with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
#         for produto in carrinho:
#             arquivo.write(produto + "\n")
# ------------------------------------------------------------------------------

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
