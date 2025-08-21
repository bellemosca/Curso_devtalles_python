# Criar uma senha com a função
# letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numeros = "0123456789"
# simbolos = "!?@#$%&*()+-=_|\/<>,.;:[]{}"
# formula simples = (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Saida: @*(123Ha
import random
import string


def password_generator(length):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = []

    for item in range(length):
        index = random.choice(caracteres)
        senha.append(index)

    return "".join(senha)


length = int(input("Quantos caracteres você quer na sua senha?"))
print("Sua senha é:", password_generator(length))
