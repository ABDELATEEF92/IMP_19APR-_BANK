from User import user
class Bank(User):
    #ABDELATEEF
    def deposit(self, amount):
        self.balance += amount
        print(f"The new balance is: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"The new balance is: {self.balance:}")
        else:
            print(" The balance was insufficient")
    def view_balance(self):
        print(f"The current balance is: {self.balance:}")
