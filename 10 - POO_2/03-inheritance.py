class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} está dormindo.")


class Dog(Animal):
    def dog_sound(self):
        print(f"{self.name} dice: AUAU!")


class Cat(Animal):
    def cat_sound(self):
        print(f"{self.name} dice: MIAU!")


firulais = Dog("firulais")
firulais.sleep()
firulais.dog_sound()


apolo = Cat("Apolo")
apolo.sleep()
apolo.cat_sound()
