# Instruções:
# Criar um programa de avaliação de potenciais candidatos com conhecimentos em Python para RH.
# O programa deve solicitar o nome, anos de experiência e habilidades.

# Avaliações:
# - Se o candidato tem mais de 3 anos de experiência e sabe Python/Django, é um excelente candidato.
# - Se o candidato tem mais de 1 anos de experiência e sabe Python/Django, é um bom candidato.
# - Se o candidato sabe Python/Django: possível candidato.
# - Se o candidato não sabe Python/Django: não é um candidato, guardar CV.

nome = input("Digite seu nome:")
experiencia = int(input("Anos de experiência no mercado: "))
linguagem = input("Insira as linguagens que você sabe (separadas por vírgula): ").split(
    ","
)

avaliando_linguagem = "Python" in linguagem or "Django" in linguagem

resultado = ""
if avaliando_linguagem:
    if experiencia >= 3:
        resultado = "Candidato excelente."
    elif experiencia >= 1:
        resultado = "Bom candidato."
    else:
        resultado = "Possível candidato."
else:
    resultado = "Não é um candidato, guardar CV."

print(f"O candidato {nome} é: {resultado}")
