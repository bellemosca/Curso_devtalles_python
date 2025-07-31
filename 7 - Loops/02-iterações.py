numeros = [1, 2, 3, 4, 5]

for n in numeros:
    print(n)

interador = iter(numeros)
# print(interador)
# print(next(interador))
# print(next(interador))
# print(next(interador))
# print(next(interador))
# print(next(interador))
# print(next(interador))

user = {"nome": "Isabelle", "idade": "33", "pode_nadar": False}

for i in user:  # colocando .values() ele retorna os valores
    print(i)  # colocando .items() retorna as chave-valor
print("-" * 30)
for i in user.items():
    key, value = i
    print(key, value)
print("-" * 30)
for key, value in user.items():
    print(key, value)
