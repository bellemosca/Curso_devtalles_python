class Person:
    especies = "Homosapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_especies(cls, new_especies):
        cls.especies = new_especies

    @staticmethod
    def is_older(age):
        return age >= 18


"""pessoa1 = Person("Isabelle", 33)
print(pessoa1.especies)
Person.change_especies("Homosapiens")
print(pessoa1.especies)

pessoa2 = Person("Fernando", 20)
print(pessoa2.especies)"""

print(Person.is_older(16))

pessoa1 = Person("Isabelle", 33)
print(Person.is_older(pessoa1.age))
