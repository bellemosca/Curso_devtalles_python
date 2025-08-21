class Person:
    def __init__(self, name, age):
        if age < 18:
            self.name = name
            self.age = age


person1 = Person("Isabelle", "33")

print(person1.name)
print(person1.age)


person2 = Person("Felipe", "37")
print(person2.name)
print(person2.age)

person3 = Person("Rafaela", "17")
print(person3.name)
print(person3.age)
