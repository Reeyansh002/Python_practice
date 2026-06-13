class BankAccount:
    def __init__(self,Balance):
        self.Balance = Balance
user = BankAccount(10000)
print(user.Balance)
user.Balance = 2000
print(user.Balance)