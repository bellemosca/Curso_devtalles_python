class BankAccount:
    interest_rate = 0.02

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print("Mudou de interesse")

    @staticmethod
    def validade_amount(amount):
        return amount > 0

    def withdraw(self, amount):
        if self.validade_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                print("Restirado com exito")
            else:
                print("Saldo insuficiente")
        else:
            print("Error: O montante deve ser maior que esse.")


account1 = BankAccount("Isabelle", 1000)
account2 = BankAccount("Felipe", 300)

print(BankAccount.interest_rate)
BankAccount.change_interest_rate(0.03)
print(BankAccount.interest_rate)

account1.withdraw(500)
account2.withdraw(-100)
