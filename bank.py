from user import User

class Bank(User):
    def __init__(self, name , age , gender , balance):
        super().__init__(name, age, gender, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"The new balance is: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"The new balance is: {self.balance}")
        else:
            print(" The balance was insufficient")
    def view_balance(self):
        print(f"The current balance is: {self.balance}")