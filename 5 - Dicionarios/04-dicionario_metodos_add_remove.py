usuario = {"nome": "Isabelle", "idade": 33, "greet": "oi mundo", "numeros": [1, 2, 3]}

# . copy()
usuario_copia = usuario.copy()
usuario_copia["idade"] = 20
print(usuario)
# print(usuario_copia)

# .pop()
usuario.pop("greet")
# print(usuario)

# . popitem()
usuario.popitem()
# print(usuario)  # elimina o último item do dicionário

# . update()
usuario.update({"nome": "Rebeca"})
usuario.update({"gatos": 2})
# print(usuario)

# .append()
usuario["skills"] = usuario.get("skills", [])
usuario["skills"].append("Python")
usuario["skills"].append("Django")
print(usuario)
