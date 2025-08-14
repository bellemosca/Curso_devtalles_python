def hello(greet="Oi", name="Convidado"):
    """
    Info: Serve para documentar na hora que eu passar o mouse em cima da função
    """
    print(f"{greet}, {name}")


# Keyword arguments
hello(name="Isabelle", greet="Oi")


# Faz parte das boas práticas
def multiply(a: float, b: float) -> float:
    """
    Info: multiplica dois números e retorna o resultado

    """
    return a * b


print(multiply(2, 3))
