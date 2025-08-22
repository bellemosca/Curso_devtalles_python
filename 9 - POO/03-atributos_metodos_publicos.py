class Person:
    especie = "Humano"

    def __init__(self, name, age):
        self.name = name  # atributos de instancia
        self.age = age

    def work(self):
        return f"{self.name} esta trabalhando muito."

    def eat(self, food):
        if food.lower() == "tacos":
            return "SUPERPOWERS"
        else:
            return "+ Energia"


pessoa1 = Person("Isabelle", 33)
print(pessoa1.name)
print(pessoa1.age)
print(pessoa1.especie)
print(pessoa1.work())
print(pessoa1.eat("ovo"))
