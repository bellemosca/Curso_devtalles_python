class Person:

    def __init__(self, name):
        self.name = name
        self._energy = 100

    def _weste_energy(self, quantity):
        self._energy -= quantity


pessoa1 = Person(
    "Isabelle",
)
print(pessoa1.name)
print(pessoa1._energy)
pessoa1._weste_energy(20)
print(pessoa1._energy)
