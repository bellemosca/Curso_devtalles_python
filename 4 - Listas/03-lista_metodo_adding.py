# Métodos de adição

num_list = [1, 2, 3, 4, 5]
# print(num_list)

num_list.append(100)
print(num_list)

# Insert
num_list.insert(1, 200)  # adiciona o elemento na posição 1
print(num_list)

# Extend
num_list.extend(
    [11, 22, 33]
)  # adiciona os elementos da lista ao final da lista original
print(num_list)
