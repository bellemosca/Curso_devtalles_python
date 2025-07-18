import datetime

nascimento = int(input("Ano de nascimento: "))
permisao_dirigir = datetime.datetime.now().year - nascimento

if permisao_dirigir >= 18:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")
