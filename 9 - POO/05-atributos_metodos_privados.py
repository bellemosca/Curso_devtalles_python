class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = "1234"  # name mangling  _NOMECLASSE__senha

    def __generate_password(self):
        return f"$${self.name}{self.age}"


pessoa1 = Person("Isabelle", 33)
print(pessoa1.name)
