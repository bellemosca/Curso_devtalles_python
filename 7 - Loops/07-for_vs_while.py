# For para interáveis, quando sabemos quando terminará
# While quando não sabemos quando termina e precisamos de uma condição

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

item = 0
while item <= len(my_list):
    print(item)
    item += 1
