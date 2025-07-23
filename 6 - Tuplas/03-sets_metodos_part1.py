# Conjuntos

# .add()
my_set = {1, 2, 3}
my_set.add(6)
my_set.add(3)
my_set.add(5)

print(my_set)

# .remove()
my_set.remove(2)
my_set.remove(6)
print(my_set)

# .discard() Não marca o erro se não existe
my_set.remove(3)
# my_set.remove(5)
# my_set.remove(7)
print(my_set)

# .pop() elimina qualquer elemento ao acaso e retorna somente ele
print(my_set.pop())
print(my_set)
