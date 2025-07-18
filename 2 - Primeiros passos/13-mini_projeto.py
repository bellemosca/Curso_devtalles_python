# Receber de forma dinámica nome, ano de nascimento, email e senha

nome = input("Digite seu nome: ").upper()
ano_nascimento = input("Digite seu ano de nascimento: ")
email = input("Digite seu email: ")
senha = input("Crie uma senha: ")
conf_senha = input("Confirme sua senha: ")

ocultar_senha = "*" * len(senha)
ocultar_conf_senha = "*" * len(conf_senha)

print("-" * 30)
print(nome)
print(2025 - int(ano_nascimento))
print(email)
print(ocultar_senha)
print(ocultar_conf_senha)
