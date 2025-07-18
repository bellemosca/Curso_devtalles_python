# and
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not
print(not True)  # False
print(not False)  # True

# Exemplos:
# and
age = 33
licenca = True

if age >= 18 and licenca:
    print("Pode dirigir.")

# or
estudante = False
membership = True

if estudante or membership:
    print("Tem um desconto especial.")

# not
admin = False

if not admin:
    print("Acesso negado.")
