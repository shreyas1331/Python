class Employee:
    name="rohan"
    salary="120000"

harry=Employee()
harry.name="Harry"
print(harry.name,harry.salary)

rohan=Employee()
rohan.name="rohannnnn"
print(rohan.name,rohan.salary)


class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"u have deposited {amount}, and the current balance is {self.balance}")

    def withdraw(self,amount):
        self.balance-=amount
        print(f"u have withdrawn {amount}, and the current balance is {self.balance}")

    def totalBal(self):
        print(f"ur total balance is {self.balance}")

shreyasAcc=BankAccount("shreyas",3000)
shreyasAcc.deposit(1000)
shreyasAcc.totalBal()
shreyasAcc.withdraw(1500)