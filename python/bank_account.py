class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def showBalance(self):
        # print(f"The Balance is : {self.__balance}")
        return self.__balance


balance = BankAccount(0)

print(f"Initial Balance: ${balance.showBalance()}")

balance.deposit(100000)

print(f"After depositing:  ${balance.showBalance()}")

balance.withdraw(2500)

print(f"After withdrawing:  ${balance.showBalance()}")
