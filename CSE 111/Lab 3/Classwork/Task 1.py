class BankAccount:
  def __init__(self,name,acc_type):
    self.user_name=name
    self.account_type=acc_type
    self.balance=1.0
def update_balance(self, new_balance):
        self.balance = new_balance
account1 = BankAccount("Bilbo", "Savings")
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")

account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")

account1.update_balance(15.75)
account2.update_balance(700.50)

print(f"New account balance of {account1.user_name} is {account1.balance}")
print(f"New account balance of {account2.user_name} is {account2.balance}")
