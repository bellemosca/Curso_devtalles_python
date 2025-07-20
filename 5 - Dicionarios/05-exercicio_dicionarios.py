estudantes = {"Isabelle": [8, 7, 9], "Felipe": [6, 5, 7], "Luis": [10, 9, 10]}

estudantes["Maria"] = estudantes.get("Maria", [6, 7, 4])

print(estudantes)

nome = "Maria"
if nome in estudantes:
    estudantes_grade = estudantes[nome]
    media = estudantes_grade[0] + estudantes_grade[1] + estudantes_grade[2] / 3
    if media >= 6.0:
        print(f"O aluno {nome} foi aprovado com média {media:.1f}!")
    else:
        print(f"O aluno {nome} foi reprovado com média {media:.1f}!")
else:
    print("Estudante não encontrado.")
