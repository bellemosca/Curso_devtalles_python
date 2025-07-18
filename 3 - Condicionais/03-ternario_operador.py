estudante = True

if estudante:
    print("Licença de estudante.")
else:
    print("Licença normal.")


get_licenca = "Licença de estudante" if estudante else "Licença normal"

print(get_licenca)
